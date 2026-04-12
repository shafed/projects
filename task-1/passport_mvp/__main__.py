"""
Запуск приложения.

Поддерживаются оба варианта:

- из корня проекта: ``python -m passport_mvp`` (каталог ``task-1`` в PYTHONPATH);
- из каталога пакета: ``python __main__.py`` — добавляем родителя пакета в ``sys.path``.
"""

from __future__ import annotations

import sys
from pathlib import Path

_pkg_dir = Path(__file__).resolve().parent
_project_root = _pkg_dir.parent
if str(_project_root) not in sys.path:
    sys.path.insert(0, str(_project_root))

from passport_mvp.app.main import main

if __name__ == "__main__":
    main()
