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
    LLM_PROVIDER: str = os.environ.get("FILROUGE_LLM_PROVIDER", "fake").strip().lower()
    COHERE_API_KEY: str = os.environ.get("COHERE_API_KEY", "")
    COHERE_MODEL: str = os.environ.get("COHERE_MODEL", "command-a-03-2025")
    GOOGLE_API_KEY: str = os.environ.get("GOOGLE_API_KEY", "")
    GEMINI_MODEL: str = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")
    OLLAMA_BASE_URL: str = os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434")
    OLLAMA_MODEL: str = os.environ.get("OLLAMA_MODEL", "llama3")

    @classmethod
    def get_db_path(cls) -> Path:
        """Retourne le chemin absolu vers la base SQLite (non utilisée en lot 0)."""
        return cls.DATA_DIR / cls.SQLITE_DB_NAME
