"""Извлечение полей из сырого текста OCR (правила + regex + эвристики)."""

from __future__ import annotations

import logging
import re
import uuid
from dataclasses import dataclass
from typing import Iterable, List

from passport_mvp.models.record import MISSING_SERIAL, PassportRecord

logger = logging.getLogger(__name__)

# --- Константы распознавания (явные «магические» пороги с пояснением) ---

# Ниже этого среднего conf Tesseract считаем OCR «слабым» для статуса manual_check
WEAK_OCR_CONF_THRESHOLD = 55.0

# Минимальная длина текста, чтобы считать документ осмысленно распознанным
MIN_MEANINGFUL_TEXT_LEN = 40


@dataclass(frozen=True)
class ExtractionContext:
    source_file: str
    ocr_confidence: float
    raw_text: str


def _normalize_ws(text: str) -> str:
    text = text.replace("\r", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def extract_cabinet_id(text: str) -> str:
    """
    Ищет идентификатор шкафа только по явным маркерам.

    Примеры: «Шкаф №12», «шкаф 3», «Cabinet ID: A-17».
    """
    patterns = [
        r"(?:шкаф|Шкаф)\s*(?:№|N|#)?\s*([A-Za-zА-Яа-я0-9\-_/]{2,40})",
        r"(?:cabinet\s*id|Cabinet\s*ID)\s*[:]\s*([A-Za-zА-Яа-я0-9\-_/]{2,40})",
    ]
    for pat in patterns:
        m = re.search(pat, text, flags=re.IGNORECASE)
        if m:
            return m.group(1).strip()
    return ""


_CERT_PATTERNS = [
    re.compile(r"(?:сертификат|Сертификат)\s*(?:соответствия)?[^\n]{0,120}", re.IGNORECASE),
    re.compile(r"(?:декларация|Декларация)\s*о\s*соответствии[^\n]{0,120}", re.IGNORECASE),
    re.compile(r"(?:сертификат|Сертификат)\s*№\s*[^\n]{5,80}", re.IGNORECASE),
]


def extract_certificate(text: str) -> str:
    """Только явные упоминания; без догадок."""
    for rx in _CERT_PATTERNS:
        m = rx.search(text)
        if m:
            return _normalize_ws(m.group(0))
    return ""


_PAGES_PATTERNS = [
    re.compile(
        r"(?:количество\s*листов|лист(?:ов|а)?|стр\.|страниц(?:а|ы)?)\s*[:]?\s*(\d{1,4})",
        re.IGNORECASE,
    ),
    re.compile(r"(\d{1,4})\s*(?:лист|листов|стр\.|страниц(?:а|ы)?)\b", re.IGNORECASE),
]


def extract_pages_or_sheets(text: str) -> str:
    for rx in _PAGES_PATTERNS:
        m = rx.search(text)
        if m:
            return m.group(1)
    return ""


_NAME_HINTS = [
    "наименование",
    "изделие",
    "оборудование",
    "паспорт",
    "документ",
]


def extract_document_name(text: str) -> str:
    """
    Эвристика MVP: ищем строку после ключевых слов или самую информативную строку.

    «Паспорт» сам по себе не подходит — берём более длинную соседнюю строку.
    """
    lines = [_normalize_ws(l) for l in text.splitlines()]
    lines = [l for l in lines if len(l) >= 6]

    lowered = [(i, l.lower()) for i, l in enumerate(lines)]

    # 1) После «наименование» / «изделие»
    for i, low in lowered:
        for hint in _NAME_HINTS:
            if hint in low and "завод" not in low:
                # берём текущую строку без префикса «Наименование:»
                cleaned = re.sub(r"^[^:]{0,30}:\s*", "", lines[i], flags=re.IGNORECASE)
                if len(cleaned) >= 8 and not re.fullmatch(r"паспорт(\s+.*)?", cleaned, re.I):
                    return cleaned[:500]
                # иначе следующая строка
                if i + 1 < len(lines) and len(lines[i + 1]) >= 8:
                    return lines[i + 1][:500]

    # 2) Первая длинная строка без типичного мусора
    noise = re.compile(r"^(стр\.|лист|дата|подпись|м\.п\.|заводской|зав\.|№\s*док)", re.I)
    for l in lines:
        if len(l) < 20:
            continue
        if noise.match(l):
            continue
        if re.fullmatch(r"паспорт(\s+.*)?", l, re.I):
            continue
        return l[:500]

    # 3) Фолбэк
    if lines:
        return lines[0][:500]
    return ""


_SERIAL_LINE = re.compile(
    r"(?:заводской|зав\.|з/н|s/n|serial)\s*(?:№|n|#)?\s*[:.]?\s*([A-Za-zА-Яа-я0-9\-_/]{4,40})",
    re.IGNORECASE,
)

# Токены, похожие на заводские номера (латиница/кириллица/цифры/дефис)
_SERIAL_TOKEN = re.compile(r"\b([A-Za-zА-Яа-я]{1,4}\d[\w\-/]{3,30})\b")


def _extract_serials_from_text(text: str) -> list[str]:
    found: list[str] = []
    for m in _SERIAL_LINE.finditer(text):
        found.append(m.group(1).strip())

    # Табличные/списочные серийники: строки, где много токенов
    for m in _SERIAL_TOKEN.finditer(text):
        token = m.group(1).strip()
        # отсекаем очевидные даты и короткий шум
        if re.fullmatch(r"\d{1,6}", token):
            continue
        found.append(token)

    # Уникальность с сохранением порядка
    uniq: list[str] = []
    seen = set()
    for s in found:
        key = s.lower()
        if key in seen:
            continue
        seen.add(key)
        uniq.append(s)
    return uniq


def _compute_row_status(
    *,
    document_name: str,
    ocr_confidence: float,
    raw_text_len: int,
    ambiguous_serial_list: bool,
) -> str:
    if ocr_confidence < WEAK_OCR_CONF_THRESHOLD or raw_text_len < MIN_MEANINGFUL_TEXT_LEN:
        return "manual_check"
    if ambiguous_serial_list:
        return "manual_check"
    if not document_name.strip():
        return "partial"
    # ``pages_or_sheets`` и ``certificate`` могут отсутствовать без потери ``ok``:
    # для MVP «основные» поля — это корректное наименование + устойчивый OCR.
    return "ok"


def extract_records(ctx: ExtractionContext) -> List[PassportRecord]:
    """
    Строит одну или несколько записей.

    Групповой паспорт: несколько заводских номеров → несколько строк с дублированием общих полей.
    Если номеров нет — одна строка с ``б/н``.
    """
    text = _normalize_ws(ctx.raw_text)
    doc_name = extract_document_name(text)
    pages = extract_pages_or_sheets(text)
    cert = extract_certificate(text)

    serials = _extract_serials_from_text(text)
    ambiguous = len(serials) > 8  # слишком много кандидатов — типичный признак шума OCR

    if not serials:
        serials = [MISSING_SERIAL]

    records: list[PassportRecord] = []
    for s in serials:
        status = _compute_row_status(
            document_name=doc_name,
            ocr_confidence=ctx.ocr_confidence,
            raw_text_len=len(text),
            ambiguous_serial_list=ambiguous,
        )
        rid = uuid.uuid4().hex[:12]
        records.append(
            PassportRecord(
                document_name=doc_name,
                serial_number=s,
                pages_or_sheets=pages,
                certificate=cert,
                source_file=ctx.source_file,
                row_status=status,
                internal_row_id=rid,
            )
        )
    return records
