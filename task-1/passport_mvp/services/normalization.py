"""Нормализация строковых полей и мягкие пост-правила после OCR."""

from __future__ import annotations

import re
import unicodedata

from passport_mvp.models.record import MISSING_SERIAL, PassportRecord


def _strip_control(s: str) -> str:
    # Убираем непечатаемые символы, сохраняя обычные переводы строк внутри значений нежелательны
    s = "".join(ch for ch in s if unicodedata.category(ch) != "Cc" or ch in "\t\n\r")
    return s.replace("\r\n", "\n").replace("\r", "\n").strip()


def normalize_record(rec: PassportRecord) -> None:
    """Приводит поля к аккуратному виду; не меняет бизнес-смысл."""
    rec.document_name = _strip_control(rec.document_name)
    rec.serial_number = _strip_control(rec.serial_number)
    rec.pages_or_sheets = _strip_control(rec.pages_or_sheets)
    rec.certificate = _strip_control(rec.certificate)
    rec.source_file = _strip_control(rec.source_file)
    rec.row_status = _strip_control(rec.row_status)

    if not rec.serial_number:
        rec.serial_number = MISSING_SERIAL

    # Нормализация пробелов внутри длинных названий
    rec.document_name = re.sub(r"\s+", " ", rec.document_name)
    rec.certificate = re.sub(r"\s+", " ", rec.certificate)


def normalize_records(records: list[PassportRecord]) -> None:
    for r in records:
        normalize_record(r)
