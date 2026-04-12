"""Генерация штрихкодов Code 128 в отдельные файлы (Pillow writer)."""

from __future__ import annotations

import logging
import re
import uuid
from pathlib import Path
from typing import Tuple

from barcode import Code128  # type: ignore[import-untyped]
from barcode.writer import ImageWriter  # type: ignore[import-untyped]

from passport_mvp.models.record import MISSING_SERIAL, PassportRecord

logger = logging.getLogger(__name__)

# Code128 в python-barcode ожидает ASCII-совместимую нагрузку для широкого круга шрифтов writer
_CODE128_SAFE = re.compile(r"^[\x20-\x7e]+$")


def _ascii_barcode_payload(raw: str, fallback_prefix: str) -> str:
    raw = raw.strip()
    if raw and _CODE128_SAFE.fullmatch(raw):
        return raw
    # Минимальная транслитерация для частых кириллических серийников
    table = str.maketrans(
        {
            "А": "A",
            "В": "B",
            "С": "C",
            "Е": "E",
            "К": "K",
            "М": "M",
            "Н": "H",
            "О": "O",
            "Р": "P",
            "Т": "T",
            "У": "Y",
            "Х": "X",
        }
    )
    candidate = raw.translate(table)
    if _CODE128_SAFE.fullmatch(candidate):
        return candidate
    short = uuid.uuid4().hex[:10].upper()
    return f"{fallback_prefix}{short}"


def generate_row_barcode_files(records: list[PassportRecord], out_dir: Path) -> None:
    """
    Для каждой строки создаёт PNG.

    ``barcode_value`` — фактически закодированная ASCII-строка (может отличаться от серийника
    при кириллице: тогда используется безопасный фолбэк).
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    writer = ImageWriter()
    writer.set_options({"module_width": 0.25, "module_height": 10.0, "quiet_zone": 3.0})

    used_names: set[str] = set()

    for rec in records:
        base_name = Path(rec.source_file).stem
        safe_base = re.sub(r"[^\w\-]+", "_", base_name, flags=re.UNICODE)[:40]
        if rec.serial_number.strip() == MISSING_SERIAL:
            payload = _ascii_barcode_payload(rec.internal_row_id or uuid.uuid4().hex, "ID")
        else:
            payload = _ascii_barcode_payload(rec.serial_number, "ID")

        rec.barcode_value = payload

        # Уникальное имя файла
        fname = f"{safe_base}_{payload[:24]}".strip("_")
        fname = re.sub(r"[^\w\-]+", "_", fname, flags=re.UNICODE)
        if fname in used_names:
            fname = f"{fname}_{uuid.uuid4().hex[:6]}"
        used_names.add(fname)

        try:
            code = Code128(payload, writer=writer)
            # python-barcode сохраняет ``{basename}.png``
            base = out_dir / fname
            code.save(str(base))
            path_png = Path(str(base) + ".png").resolve()
            rec.barcode_file = str(path_png)
        except Exception as e:  # noqa: BLE001 — MVP: не валим пакетную обработку
            logger.exception("Не удалось создать штрихкод строки для %s: %s", rec.source_file, e)
            rec.barcode_file = ""
            rec.barcode_value = payload


def generate_cabinet_barcode(cabinet_id: str, out_dir: Path) -> Tuple[str, str]:
    """
    Возвращает (barcode_value, path_png). Пустой cabinet_id → ("", "").
    """
    cabinet_id = cabinet_id.strip()
    if not cabinet_id:
        return "", ""

    out_dir.mkdir(parents=True, exist_ok=True)
    writer = ImageWriter()
    writer.set_options({"module_width": 0.25, "module_height": 12.0, "quiet_zone": 3.0})

    payload = _ascii_barcode_payload(cabinet_id, "CAB")
    safe = re.sub(r"[^\w\-]+", "_", payload, flags=re.UNICODE)[:60]
    base = out_dir / f"cabinet_{safe}"
    try:
        code = Code128(payload, writer=writer)
        code.save(str(base))
        path_png = Path(str(base) + ".png").resolve()
        return payload, str(path_png)
    except Exception as e:  # noqa: BLE001
        logger.exception("Не удалось создать штрихкод шкафа: %s", e)
        return payload, ""


def attach_cabinet_barcode_to_rows(records: list[PassportRecord], cabinet_id: str, barcode_path: str) -> None:
    for r in records:
        r.cabinet_id = cabinet_id.strip()
        r.cabinet_barcode_file = barcode_path
