"""Choix du modèle ADK : simulation locale, Gemini, Cohere ou Ollama."""

import os
from collections.abc import AsyncGenerator

from google.adk.models.base_llm import BaseLlm
from google.adk.models.llm_request import LlmRequest
from google.adk.models.llm_response import LlmResponse
from google.genai import types

from filrouge.adapters.fake_text_generator import FakeTextGenerator
from filrouge.config import AppConfig
from filrouge.domain.exceptions import ConfigurationError


class LocalAdkModel(BaseLlm):
    """Exécute la vraie boucle ADK avec une réponse déterministe sans réseau."""

    model: str = "fake-simulator-lot0"

    async def generate_content_async(
        self, llm_request: LlmRequest, stream: bool = False
    ) -> AsyncGenerator[LlmResponse, None]:
        del stream
        message = next((content for content in reversed(llm_request.contents) if content.role == "user"), None)
        text = "".join(part.text or "" for part in (message.parts or [])) if message else ""
        reply = FakeTextGenerator().generate_reply(text)
        yield LlmResponse(content=types.Content(role="model", parts=[types.Part(text=reply.text)]))


def build_adk_model(provider: str | None = None) -> BaseLlm:
    """Construit le modèle sans effectuer d'appel distant."""
    provider = AppConfig.LLM_PROVIDER if provider is None else provider
    if provider == "fake":
        return LocalAdkModel()
    if provider == "gemini":
        if not AppConfig.GOOGLE_API_KEY.strip():
            raise ConfigurationError("GOOGLE_API_KEY est obligatoire pour Gemini.")
        from google.adk.models.google_llm import Gemini

        return Gemini(
            model=AppConfig.GEMINI_MODEL,
            client_kwargs={"api_key": AppConfig.GOOGLE_API_KEY, "vertexai": False},
        )
    if provider in {"cohere", "ollama"}:
        # LiteLLM est chargé uniquement pour ces profils. Son catalogue de coûts
        # local évite un téléchargement implicite au premier import.
        os.environ.setdefault("LITELLM_LOCAL_MODEL_COST_MAP", "True")
        from google.adk.models.lite_llm import LiteLlm

        if provider == "cohere":
            if not AppConfig.COHERE_API_KEY.strip():
                raise ConfigurationError("COHERE_API_KEY est obligatoire pour Cohere.")
            return LiteLlm(model=f"cohere_chat/{AppConfig.COHERE_MODEL}", api_key=AppConfig.COHERE_API_KEY)
        return LiteLlm(model=f"ollama_chat/{AppConfig.OLLAMA_MODEL}", api_base=AppConfig.OLLAMA_BASE_URL)
    raise ConfigurationError(f"Fournisseur inconnu : {provider!r}. Choisir fake, cohere, gemini ou ollama.")
