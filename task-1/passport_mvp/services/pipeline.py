"""Оркестрация: файлы → изображения → OCR → извлечение → нормализация."""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, List, Optional

from PIL import Image

from passport_mvp.config.settings import AppSettings, DEFAULT_SETTINGS
from passport_mvp.models.record import PassportRecord
from passport_mvp.services import extraction
from passport_mvp.services.extraction import ExtractionContext
from passport_mvp.services.normalization import normalize_records
from passport_mvp.services.ocr_engine import ocr_image, tesseract_available
from passport_mvp.services.preprocessor import preprocess_for_ocr

logger = logging.getLogger(__name__)


@dataclass
class ProcessingStats:
    files_total: int = 0
    files_ok: int = 0
    rows_total: int = 0
    errors: list[str] = field(default_factory=list)
    cabinet_guess: str = ""


ProgressCallback = Callable[[str], None]


def _pdf_to_images(path: Path, dpi: int) -> List[Image.Image]:
    from pdf2image import convert_from_path  # локальный импорт — ясная ошибка если нет зависимости

    try:
        return convert_from_path(str(path), dpi=dpi)
    except Exception as e:  # noqa: BLE001
        raise RuntimeError(
            "Не удалось преобразовать PDF в изображения. "
            "Проверьте установку Poppler (Windows: poppler в PATH; Linux: poppler-utils; macOS: poppler)."
        ) from e


def _load_image(path: Path) -> Image.Image:
    return Image.open(path).convert("RGB")


def process_files(
    files: list[Path],
    settings: AppSettings = DEFAULT_SETTINGS,
    on_progress: Optional[ProgressCallback] = None,
) -> tuple[list[PassportRecord], ProcessingStats]:
    """
    Обрабатывает список файлов и возвращает плоский список записей + статистику.

    Повреждённые/чужие файлы не роняют цикл: ошибка попадает в ``stats.errors``.
    """
    stats = ProcessingStats(files_total=len(files))
    all_records: list[PassportRecord] = []

    if not tesseract_available():
        stats.errors.append("Tesseract не найден в PATH — OCR недоступен.")
        return all_records, stats

    for fp in files:
        msg = f"Обработка: {fp.name}"
        logger.info(msg)
        if on_progress:
            on_progress(msg)

        try:
            images: list[Image.Image] = []
            if fp.suffix.lower() == ".pdf":
                images = _pdf_to_images(fp, settings.pdf_render_dpi)
            else:
                images = [_load_image(fp)]

            parts: list[str] = []
            confs: list[float] = []
            for im in images:
                prep = preprocess_for_ocr(im, min_width=settings.min_ocr_width_px)
                text, conf = ocr_image(prep, lang=settings.tesseract_lang)
                parts.append(text)
                confs.append(conf)

            merged = "\n\n".join(parts)
            avg_conf = sum(confs) / len(confs) if confs else 0.0

            guess = extraction.extract_cabinet_id(merged)
            if guess and not stats.cabinet_guess:
                stats.cabinet_guess = guess

            ctx = ExtractionContext(source_file=fp.name, ocr_confidence=avg_conf, raw_text=merged)
            recs = extraction.extract_records(ctx)
            normalize_records(recs)
            all_records.extend(recs)

            stats.files_ok += 1
            stats.rows_total += len(recs)
        except Exception as e:  # noqa: BLE001
            err = f"{fp.name}: {e}"
            logger.exception("Ошибка обработки файла %s", fp)
            stats.errors.append(err)

    return all_records, stats
