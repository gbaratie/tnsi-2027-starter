"""Modèles du domaine pour les interactions de chat (Lot 0 - Simulation)."""

from dataclasses import dataclass
from datetime import UTC, datetime


@dataclass(frozen=True)
class ChatReply:
    """Réponse générée par un composant d'IA (ou simulateur)."""

    text: str
    is_simulation: bool = True
    model_name: str = "fake-simulator-lot0"
    created_at: str = datetime.now(UTC).isoformat()
