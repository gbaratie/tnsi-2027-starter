"""Port pour la génération de texte (LLM ou Simulateur)."""

from typing import Protocol

from filrouge.domain.chat import ChatReply


class TextGeneratorPort(Protocol):
    """Contrat de génération de texte."""

    def generate_reply(self, message: str) -> ChatReply:
        """Génère une réponse textuelle à partir du message utilisateur."""
        ...
