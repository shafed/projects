"""Модель строки результата (паспорт / позиция в групповом паспорте)."""

from __future__ import annotations

from dataclasses import dataclass, field, fields
from typing import Any, Mapping


MISSING_SERIAL = "б/н"


@dataclass
class PassportRecord:
    """
    Одна строка таблицы: один заводской номер (или ``б/н``).

    Поля ``barcode_*`` и ``cabinet_*`` заполняются после генерации штрихкодов.
    """

    document_name: str
    serial_number: str
    pages_or_sheets: str
    certificate: str
    source_file: str
    row_status: str

    barcode_value: str = ""
    barcode_file: str = ""
    cabinet_id: str = ""
    cabinet_barcode_file: str = ""

    # Служебные (не экспортируем в CSV по умолчанию, но полезны для отладки)
    internal_row_id: str = field(default="", repr=False)

    def as_export_row(self) -> dict[str, Any]:
        """Плоский словарь для CSV/XLSX."""
        return {
            "document_name": self.document_name,
            "serial_number": self.serial_number,
            "pages_or_sheets": self.pages_or_sheets,
            "certificate": self.certificate,
            "source_file": self.source_file,
            "row_status": self.row_status,
            "barcode_value": self.barcode_value,
            "barcode_file": self.barcode_file,
            "cabinet_id": self.cabinet_id,
            "cabinet_barcode_file": self.cabinet_barcode_file,
        }

    @staticmethod
    def export_columns() -> list[str]:
        return [
            "document_name",
            "serial_number",
            "pages_or_sheets",
            "certificate",
            "source_file",
            "row_status",
            "barcode_value",
            "barcode_file",
            "cabinet_id",
            "cabinet_barcode_file",
        ]

    @classmethod
    def from_mapping(cls, data: Mapping[str, Any]) -> PassportRecord:
        known = {f.name for f in fields(cls)}
        kwargs: dict[str, Any] = {}
        for name in known:
            if name not in data:
                continue
            val = data.get(name)
            kwargs[name] = "" if val is None else str(val)
        return cls(**kwargs)  # type: ignore[arg-type]
