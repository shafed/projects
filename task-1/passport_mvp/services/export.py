"""Экспорт таблицы в CSV и XLSX."""

from __future__ import annotations

import csv
import logging
from pathlib import Path
from typing import Iterable

from openpyxl import Workbook

from passport_mvp.models.record import PassportRecord

logger = logging.getLogger(__name__)


def export_csv(records: Iterable[PassportRecord], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    cols = PassportRecord.export_columns()
    with path.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in records:
            w.writerow(r.as_export_row())


def export_xlsx(records: Iterable[PassportRecord], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    wb = Workbook()
    ws = wb.active
    ws.title = "results"
    cols = PassportRecord.export_columns()
    ws.append(cols)
    for r in records:
        row = [r.as_export_row()[c] for c in cols]
        ws.append(row)
    wb.save(path)
