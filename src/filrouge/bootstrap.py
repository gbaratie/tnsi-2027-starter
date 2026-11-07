"""Bootstrap : assemblage et injection des dépendances."""

from dataclasses import dataclass

from filrouge.adapters.fake_text_generator import FakeTextGenerator
from filrouge.application.use_cases.chat_with_simulation import ChatWithSimulation


@dataclass
class ApplicationContainer:
    """Conteneur des use cases instanciés."""

    chat_with_simulation: ChatWithSimulation


def create_application() -> ApplicationContainer:
    """Fabrique et assemble les adaptateurs et use cases du Lot 0."""
    text_generator = FakeTextGenerator()

    return ApplicationContainer(
        chat_with_simulation=ChatWithSimulation(text_generator=text_generator),
    )
