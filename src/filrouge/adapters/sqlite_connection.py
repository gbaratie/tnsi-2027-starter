"""Infrastructure SQLite partagée (Lot 0 : aucune table, aucun usage métier).

Ce module prépare les lots suivants : il crée le dossier de données et fournit
une connexion qui est réellement fermée (le `with sqlite3.connect(...)` natif
valide la transaction mais ne ferme pas la connexion).
"""

import sqlite3
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path

from filrouge.domain.exceptions import StorageError


@contextmanager
def open_connection(db_path: str | Path) -> Iterator[sqlite3.Connection]:
    """Ouvre une connexion SQLite, valide ou annule la transaction, puis la ferme."""
    path = Path(db_path)
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        conn = sqlite3.connect(path)
    except (OSError, sqlite3.Error) as e:
        raise StorageError(
            message="Impossible d'ouvrir la base de données locale.",
            details=f"Chemin: {path}, Erreur: {e}",
        ) from e

    try:
        yield conn
        conn.commit()
    except sqlite3.Error as e:
        conn.rollback()
        raise StorageError(
            message="Erreur lors de l'accès à la base de données locale.",
            details=str(e),
        ) from e
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
