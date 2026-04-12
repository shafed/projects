"""Настройка логирования в файл и консоль."""

from __future__ import annotations

import logging
from pathlib import Path


def setup_logging(log_dir: Path, level: int = logging.INFO) -> None:
    """
    Создаёт каталог логов и настраивает корневой логгер.

    Файл: ``log_dir / app.log`` (ротация в MVP не используется — проще для защиты).
    """
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "app.log"

    root = logging.getLogger()
    root.setLevel(level)

    # Избегаем дублирования обработчиков при повторном вызове (например, в тестах)
    if root.handlers:
        return

    fmt = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    fh = logging.FileHandler(log_file, encoding="utf-8")
    fh.setLevel(level)
    fh.setFormatter(fmt)

    ch = logging.StreamHandler()
    ch.setLevel(level)
    ch.setFormatter(fmt)

    root.addHandler(fh)
    root.addHandler(ch)
