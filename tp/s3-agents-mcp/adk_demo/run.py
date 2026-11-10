"""Observer le même exemple sans navigateur : python tp/s3-agents-mcp/adk_demo/run.py."""
import asyncio

from agent import catalogue, root_agent
from google.adk.agents.run_config import RunConfig
from google.adk.runners import InMemoryRunner
from google.genai import types


async def main():
    runner = InMemoryRunner(agent=root_agent, app_name="s3_discovery")
    try:
        async with asyncio.timeout(30):
            await catalogue.get_tools()  # Une indisponibilité MCP doit être visible.
            session = await runner.session_service.create_session(app_name="s3_discovery", user_id="local")
            async for event in runner.run_async(
                user_id="local", session_id=session.id,
                new_message=types.Content(role="user", parts=[types.Part(text="Quels morceaux focus puis-je écouter ?")]),
                run_config=RunConfig(max_llm_calls=6),
            ):
                print(event.model_dump_json(exclude_none=True))
    finally:
        await runner.close()


if __name__ == "__main__":
    asyncio.run(main())
