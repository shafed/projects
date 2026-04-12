"""Изолированный слой OCR (Tesseract)."""

from __future__ import annotations

import logging
import shutil
from typing import Tuple

import pytesseract
from PIL import Image

logger = logging.getLogger(__name__)


def tesseract_available() -> bool:
    return shutil.which("tesseract") is not None


def ocr_image(pil_image: Image.Image, lang: str = "rus+eng") -> Tuple[str, float]:
    """
    Выполняет OCR и возвращает (текст, средняя уверенность 0..100).

    Уверенность берётся из ``image_to_data`` по символам/словам с conf != -1.
    Если движок не вернул conf, возвращаем 50.0 как нейтральное значение MVP.
    """
    if not tesseract_available():
        raise RuntimeError(
            "Исполняемый файл tesseract не найден в PATH. "
            "Установите Tesseract OCR для вашей ОС и перезапустите терминал."
        )

    data = pytesseract.image_to_data(
        pil_image,
        lang=lang,
        output_type=pytesseract.Output.DICT,
    )
    confs: list[float] = []
    for c in data.get("conf", []):
        try:
            v = float(c)
        except (TypeError, ValueError):
            continue
        if v >= 0:
            confs.append(v)

    text = pytesseract.image_to_string(pil_image, lang=lang) or ""
    text = text.replace("\x0c", "\n")

    if not confs:
        return text, 50.0
    return text, sum(confs) / len(confs)
