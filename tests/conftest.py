"""Configuration des tests pytest."""

import sys
from pathlib import Path

# Ajout de src/ au PYTHONPATH pour les tests
SRC_PATH = Path(__file__).resolve().parent.parent / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))
