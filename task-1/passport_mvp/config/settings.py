"""Пути и параметры по умолчанию (без жёстко зашитых абсолютных путей)."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class AppSettings:
    """Настройки приложения: выходные каталоги и параметры OCR/рендеринга PDF."""

    # Базовая папка вывода относительно текущей рабочей директории при запуске
    output_root: Path = Path("output")
    barcodes_subdir: str = "barcodes"
    logs_subdir: str = "logs"
    results_csv_name: str = "results.csv"
    results_xlsx_name: str = "results.xlsx"

    # Рендер PDF: баланс качества/скорости для MVP
    pdf_render_dpi: int = 200
    # Минимальная ширина изображения для OCR (если меньше — аккуратное увеличение)
    min_ocr_width_px: int = 1200
    # Языки Tesseract
    tesseract_lang: str = "rus+eng"

    @property
    def output_dir(self) -> Path:
        return self.output_root

    @property
    def barcodes_dir(self) -> Path:
        return self.output_root / self.barcodes_subdir

    @property
    def logs_dir(self) -> Path:
        return self.output_root / self.logs_subdir


DEFAULT_SETTINGS = AppSettings()
