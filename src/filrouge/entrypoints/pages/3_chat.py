"""Page 3 : 💬 Interface de Chat (Assistant Métier)."""

import streamlit as st

from filrouge.bootstrap import create_application
from filrouge.domain.exceptions import ValidationError


def get_app():
    if "app_container" not in st.session_state:
        st.session_state["app_container"] = create_application()
    return st.session_state["app_container"]


app = get_app()

st.header("💬 Interface de Chat — Assistant Métier")

st.info(
    "🏷️ **Simulation locale — aucun modèle externe appelé.**\n\n"
    "Ce simulateur valide la circulation des messages à travers l'architecture sans nécessiter de clé API ni de réseau. "
    "Les modèles réels (Cohere, Ollama) seront branchés à partir de la Séance 2."
)

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Suggestions de questions d'exemple
suggested_questions = [
    "Quel est le plafond d'indemnisation sans franchise ?",
    "Quelles sont les clauses d'exclusion applicables ?",
    "Comment contacter l'assistance en cas d'urgence ?",
]

st.caption("💡 **Questions suggérées :**")
cols = st.columns(len(suggested_questions))
for i, q in enumerate(suggested_questions):
    if cols[i].button(f"🗨️ {q[:32]}...", key=f"quick_q_{i}", help=q):
        st.session_state["suggested_prompt"] = q

# Affichage de l'historique
for sender, message, is_sim in st.session_state["chat_history"]:
    with st.chat_message(sender):
        if is_sim:
            st.caption("⚙️ Réponse simulée")
        st.markdown(message)

default_prompt = st.session_state.pop("suggested_prompt", None)
user_input = st.chat_input("Posez une question sur votre domaine métier...") or default_prompt

if user_input:
    st.session_state["chat_history"].append(("user", user_input, False))
    with st.chat_message("user"):
        st.markdown(user_input)

    try:
        reply = app.chat_with_simulation.execute(user_input)
        st.session_state["chat_history"].append(("assistant", reply.text, reply.is_simulation))
        with st.chat_message("assistant"):
            st.caption("⚙️ Réponse simulée")
            st.markdown(reply.text)
    except ValidationError as e:
        st.error(f"❌ {e.message}")
