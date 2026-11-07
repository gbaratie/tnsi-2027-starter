"""Générateur de texte simulé (Lot 0 - Zéro clé / Zéro réseau)."""

from filrouge.domain.chat import ChatReply


class FakeTextGenerator:
    """Générateur déterministe pour tester le flux de découverte GenAI sans API externe."""

    def __init__(self, prefix: str = "Simulation — aucun modèle externe appelé") -> None:
        self.prefix = prefix

    def generate_reply(self, message: str) -> ChatReply:
        """Génère une réponse déterministe simulant un retour LLM."""
        reply_content = (
            f"[{self.prefix}]\n\n"
            f"Bonjour ! J'ai bien reçu votre message : « {message} ».\n\n"
            "En Séance 1, nous validons le socle applicatif local et la circulation "
            "des flux dans l'architecture hexagonale. Ce composant est un adaptateur de test (Fake). "
            "En Séance 2, nous connecterons ce port à de véritables modèles (Cohere ou Ollama)."
        )
        return ChatReply(
            text=reply_content,
            is_simulation=True,
            model_name="fake-simulator-lot0",
        )
