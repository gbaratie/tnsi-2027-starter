"""Adaptateur ADK du port de génération ; les types ADK restent à la frontière."""

import asyncio

from google.adk.agents import Agent
from google.adk.agents.run_config import RunConfig
from google.adk.runners import InMemoryRunner
from google.genai import types

from filrouge.adapters.adk_models import build_adk_model
from filrouge.config import AppConfig
from filrouge.domain.chat import ChatReply
from filrouge.domain.exceptions import GenerationError


def create_chat_agent(provider: str | None = None) -> Agent:
    """Agent sans tool utilisé en S1 et S2 ; ses concepts sont étudiés en S3."""
    return Agent(
        name="course_assistant",
        model=build_adk_model(provider),
        instruction="Réponds en français. Respecte les sources et les consignes du message. Signale tes limites.",
    )


class AdkTextGenerator:
    def __init__(self, provider: str | None = None, timeout_seconds: float = 30) -> None:
        self.provider = AppConfig.LLM_PROVIDER if provider is None else provider
        self.agent = create_chat_agent(self.provider)
        self.timeout_seconds = timeout_seconds

    def generate_reply(self, message: str) -> ChatReply:
        try:
            return asyncio.run(self._generate(message))
        except Exception as error:
            # Les exceptions SDK peuvent contenir requêtes, données et clés.
            # L'UI affiche une erreur bornée sans réessayer avec un fake.
            raise GenerationError(
                f"Échec ADK ({self.provider}, {type(error).__name__}). Vérifiez la configuration et le quota."
            ) from error

    async def _generate(self, message: str) -> ChatReply:
        runner = InMemoryRunner(agent=self.agent, app_name="filrouge")
        try:
            async with asyncio.timeout(self.timeout_seconds):
                session = await runner.session_service.create_session(app_name="filrouge", user_id="local")
                answer = ""
                async for event in runner.run_async(
                    user_id="local", session_id=session.id,
                    new_message=types.Content(role="user", parts=[types.Part(text=message)]),
                    run_config=RunConfig(max_llm_calls=1),
                ):
                    if event.error_code:
                        raise RuntimeError("Erreur modèle ADK")
                    if event.is_final_response() and event.content:
                        answer = "".join(part.text or "" for part in event.content.parts or [] if not part.thought)
                if not answer.strip():
                    raise RuntimeError("Aucune réponse finale ADK")
                return ChatReply(text=answer, is_simulation=self.provider == "fake", model_name=self.agent.model.model)
        finally:
            await runner.close()
