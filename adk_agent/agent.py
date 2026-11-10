"""L'interface de développement ADK utilise le même agent que Streamlit."""

from filrouge.adapters.adk_text_generator import create_chat_agent

root_agent = create_chat_agent()
