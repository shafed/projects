"""Загрузка и фильтрация входных файлов (PDF, изображения)."""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Iterable

logger = logging.getLogger(__name__)

SUPPORTED_EXTENSIONS = {".pdf", ".png", ".jpg", ".jpeg"}


def is_supported_file(path: Path) -> bool:
    return path.suffix.lower() in SUPPORTED_EXTENSIONS


def iter_files_from_paths(paths: Iterable[Path]) -> list[Path]:
    """Разворачивает только файлы; папки обрабатываются на уровне GUI/pipeline."""
    out: list[Path] = []
    for p in paths:
        try:
            rp = p.resolve()
        except OSError as e:
            logger.warning("Не удалось resolve путь %s: %s", p, e)
            continue
        if rp.is_file() and is_supported_file(rp):
            out.append(rp)
        elif rp.is_file():
            logger.info("Пропуск неподдерживаемого файла: %s", rp.name)
    return out


def iter_files_in_directory(directory: Path, recursive: bool = False) -> list[Path]:
    """Собирает поддерживаемые файлы из каталога."""
    if not directory.is_dir():
        logger.warning("Каталог не найден или не каталог: %s", directory)
        return []

    pattern = "**/*" if recursive else "*"
    found: list[Path] = []
    for p in directory.glob(pattern):
        if p.is_file() and is_supported_file(p):
            found.append(p.resolve())
    found.sort(key=lambda x: x.name.lower())
    return found
