"""Point d'entrée racine de l'application Streamlit."""

import sys
from pathlib import Path

# S'assure que le dossier src est dans le PYTHONPATH
SRC_PATH = Path(__file__).resolve().parent / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from filrouge.entrypoints.streamlit_app import main

if __name__ == "__main__":
    main()
