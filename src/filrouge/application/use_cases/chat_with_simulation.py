"""Use case de chat de découverte (Lot 0 - Simulation)."""

from filrouge.application.ports.text_generator import TextGeneratorPort
from filrouge.domain.chat import ChatReply
from filrouge.domain.exceptions import ValidationError


class ChatWithSimulation:
    """Interagit avec le générateur simulé sans persistance de conversation."""

    def __init__(self, text_generator: TextGeneratorPort) -> None:
        self._text_generator = text_generator

    def execute(self, message: str) -> ChatReply:
        """Valide la saisie et délègue au générateur."""
        cleaned_message = message.strip() if isinstance(message, str) else ""

        if not cleaned_message:
            raise ValidationError(
                message="Le message utilisateur ne peut pas être vide.",
                fields={"message": "Veuillez saisir une question ou un message."},
            )

        return self._text_generator.generate_reply(cleaned_message)
