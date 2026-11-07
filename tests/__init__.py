"""Suite de tests du socle applicatif Fil Rouge."""

import sys
from pathlib import Path

# Assure que src/ est dans sys.path pour pytest et unittest
SRC_PATH = Path(__file__).resolve().parent.parent / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))
