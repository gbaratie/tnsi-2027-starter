"""Tests unitaires du chat de découverte et du FakeTextGenerator."""

import sys
import unittest
from pathlib import Path

SRC_PATH = Path(__file__).resolve().parent.parent / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from filrouge.adapters.fake_text_generator import FakeTextGenerator
from filrouge.application.use_cases.chat_with_simulation import ChatWithSimulation
from filrouge.domain.exceptions import ValidationError


class TestChatUseCase(unittest.TestCase):
    def test_chat_with_simulation_success(self):
        fake_generator = FakeTextGenerator()
        use_case = ChatWithSimulation(text_generator=fake_generator)

        reply = use_case.execute("Comment fonctionne le projet ?")

        self.assertTrue(reply.is_simulation)
        self.assertEqual(reply.model_name, "fake-simulator-lot0")
        self.assertIn("Comment fonctionne le projet ?", reply.text)
        self.assertIn("Simulation — aucun modèle externe appelé", reply.text)

    def test_chat_with_empty_message_raises_validation_error(self):
        fake_generator = FakeTextGenerator()
        use_case = ChatWithSimulation(text_generator=fake_generator)

        with self.assertRaises(ValidationError) as ctx:
            use_case.execute("   ")

        self.assertIn("message", ctx.exception.fields)


if __name__ == "__main__":
    unittest.main()
