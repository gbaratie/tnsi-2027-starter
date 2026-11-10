"""Bootstrap : assemblage et injection des dépendances."""

from dataclasses import dataclass

from filrouge.adapters.adk_text_generator import AdkTextGenerator
from filrouge.application.ports.text_generator import TextGeneratorPort
from filrouge.application.use_cases.chat_with_simulation import ChatWithSimulation


@dataclass
class ApplicationContainer:
    """Conteneur des use cases instanciés."""

    chat_with_simulation: ChatWithSimulation


def build_text_generator(provider: str | None = None) -> TextGeneratorPort:
    """Même runtime ADK pour le mode local et les fournisseurs réels."""
    return AdkTextGenerator(provider)


def create_application() -> ApplicationContainer:
    """Fabrique et assemble les adaptateurs et use cases du Lot 0."""
    text_generator = build_text_generator()

    return ApplicationContainer(
        chat_with_simulation=ChatWithSimulation(text_generator=text_generator),
    )
