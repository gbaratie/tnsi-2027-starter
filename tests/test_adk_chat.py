"""Vraie exécution ADK sans clé, contrat commun et erreurs sans repli."""

import socket
from unittest.mock import patch

import pytest
from google.adk.models.base_llm import BaseLlm
from google.adk.models.llm_response import LlmResponse
from google.genai import types

from filrouge.adapters.adk_models import build_adk_model
from filrouge.adapters.adk_text_generator import AdkTextGenerator
from filrouge.bootstrap import create_application
from filrouge.config import AppConfig
from filrouge.domain.exceptions import ConfigurationError, GenerationError, ValidationError


def test_default_chat_runs_adk_without_network_or_creating_data(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(AppConfig, "LLM_PROVIDER", "fake")
    with patch.object(socket.socket, "connect", side_effect=AssertionError("Réseau interdit")):
        app = create_application()
        reply = app.chat_with_simulation.execute("Première question unique")
        second = app.chat_with_simulation.execute("Deuxième question")
    assert isinstance(app.chat_with_simulation._text_generator, AdkTextGenerator)
    assert reply.is_simulation and "Première question unique" in reply.text
    assert "Deuxième question" in second.text
    assert "Première question unique" not in second.text
    assert not list(tmp_path.iterdir())


@pytest.mark.parametrize("provider", ["cohere", "gemini"])
def test_missing_live_key_is_configuration_error(provider, monkeypatch):
    monkeypatch.setattr(AppConfig, "COHERE_API_KEY", "")
    monkeypatch.setattr(AppConfig, "GOOGLE_API_KEY", "")
    with pytest.raises(ConfigurationError):
        build_adk_model(provider)


def test_unknown_provider_is_not_a_simulation():
    with pytest.raises(ConfigurationError):
        build_adk_model("unknown")


def test_oversized_question_is_rejected_before_model_call():
    app = create_application()
    with pytest.raises(ValidationError):
        app.chat_with_simulation.execute("x" * 4001)


@pytest.mark.parametrize("provider,prefix", [("cohere", "cohere_chat/"), ("gemini", "gemini-"),
                                            ("ollama", "ollama_chat/")])
def test_provider_configuration_without_calling_service(provider, prefix, monkeypatch):
    monkeypatch.setattr(AppConfig, "COHERE_API_KEY", "test-key")
    monkeypatch.setattr(AppConfig, "GOOGLE_API_KEY", "test-key")
    model = build_adk_model(provider)
    assert model.model.startswith(prefix)


class ErrorModel(BaseLlm):
    model: str = "test-error"

    async def generate_content_async(self, llm_request, stream=False):
        raise RuntimeError("sensitive-request-or-key")
        yield  # pragma: no cover


class SuccessModel(BaseLlm):
    model: str = "test-live"

    async def generate_content_async(self, llm_request, stream=False):
        yield LlmResponse(content=types.Content(role="model", parts=[types.Part(text="Réponse de test")]))


def test_live_response_is_not_labelled_simulation():
    generator = AdkTextGenerator("fake")
    generator.provider = "gemini"
    generator.agent.model = SuccessModel()
    assert not generator.generate_reply("Question").is_simulation


def test_model_error_is_visible_sanitized_and_never_falls_back():
    generator = AdkTextGenerator("fake")
    generator.agent.model = ErrorModel()
    with pytest.raises(GenerationError) as error:
        generator.generate_reply("Question")
    assert "RuntimeError" in error.value.message
    assert "sensitive" not in error.value.message
