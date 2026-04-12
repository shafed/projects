"""Предобработка изображений перед OCR (масштаб, контраст, бинаризация)."""

from __future__ import annotations

import logging
from PIL import Image, ImageEnhance, ImageOps

logger = logging.getLogger(__name__)


def _to_grayscale(img: Image.Image) -> Image.Image:
    return ImageOps.grayscale(img)


def _maybe_upscale(img: Image.Image, min_width: int) -> Image.Image:
    w, h = img.size
    if w >= min_width:
        return img
    scale = min_width / float(w)
    new_size = (int(w * scale), int(h * scale))
    # LANCZOS даёт более читаемый текст на сканах при увеличении
    return img.resize(new_size, Image.Resampling.LANCZOS)


def preprocess_for_ocr(pil_image: Image.Image, min_width: int = 1200) -> Image.Image:
    """
    Цепочка MVP: grayscale → лёгкое повышение контраста → автоконтраст → Otsu-подобная пороговая.

    Порог Otsu реализован через ImageOps.autocontrast + point для жёсткой бинаризации,
    что устойчиво на «средних» сканах без тяжёлых зависимостей вроде OpenCV.
    """
    img = pil_image.convert("RGB")
    img = _to_grayscale(img)
    img = _maybe_upscale(img, min_width)
    img = ImageEnhance.Contrast(img).enhance(1.35)
    img = ImageOps.autocontrast(img)
    # Бинаризация по медиане яркости (простая альтернатива Otsu)
    hist = img.histogram()
    total = sum(hist)
    cum = 0
    median_val = 0
    half = total // 2
    for i, c in enumerate(hist):
        cum += c
        if cum >= half:
            median_val = i
            break
    threshold = max(10, min(245, int(median_val * 0.95)))
    img = img.point(lambda p, t=threshold: 255 if p > t else 0)
    return img
