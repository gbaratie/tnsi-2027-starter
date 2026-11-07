"""Configuration centralisée de l'application."""

import os
from pathlib import Path

from dotenv import load_dotenv

# Charge les variables depuis un éventuel .env local
load_dotenv()


class AppConfig:
    """Paramètres applicatifs résolus au démarrage."""

    DATA_DIR: Path = Path(os.environ.get("FILROUGE_DATA_DIR", "./data")).resolve()
    SQLITE_DB_NAME: str = "app.sqlite3"

    @classmethod
    def get_db_path(cls) -> Path:
        """Retourne le chemin absolu vers la base SQLite (non utilisée en lot 0)."""
        return cls.DATA_DIR / cls.SQLITE_DB_NAME
