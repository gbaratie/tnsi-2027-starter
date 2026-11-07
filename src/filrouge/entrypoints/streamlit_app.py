"""Point d'entrée de l'interface Streamlit (Couche Entrypoints).

Configure la navigation multipage native vers les vues situées dans `entrypoints/pages/`.
"""

from pathlib import Path

import streamlit as st


def render_sidebar_greeting():
    """Composant de salutation logé discrètement en bas de la barre latérale (Capsule C4 SRP)."""
    st.sidebar.markdown("---")
    with st.sidebar.expander("👋 Salutation rapide (Capsule C4)", expanded=False):
        name = st.text_input("Prénom", value=st.session_state.get("greeting_name", ""), key="sb_greet_name")
        lang = st.selectbox("Langue", ["fr", "en", "es"], key="sb_greet_lang")

        if st.button("Dire bonjour", key="sb_greet_btn"):
            if lang == "fr":
                msg = f"Bonjour, {name} !"
            elif lang == "en":
                msg = f"Hello, {name.upper()} !"  # Bug intentionnel de casse
            else:
                msg = f"Hola, {name} !"
            st.session_state["last_greeting"] = msg
            st.success(msg)
            print(f"[GREETING] {msg} — langue={lang}")


def main():
    """Configure et lance la navigation multipage de Streamlit."""
    st.set_page_config(
        page_title="TNSI Dauphine 2027 — Vitrine & Assistant Métier",
        page_icon="🎓",
        layout="wide",
    )

    pages_dir = Path(__file__).resolve().parent / "pages"

    page_project = st.Page(str(pages_dir / "1_projet.py"), title="Projet", icon="🚀", default=True)
    page_guide = st.Page(str(pages_dir / "2_guide_streamlit.py"), title="Guide Streamlit", icon="💡")
    page_chat = st.Page(str(pages_dir / "3_chat.py"), title="Interface de Chat", icon="💬")
    page_roadmap = st.Page(str(pages_dir / "4_deroule.py"), title="Déroulé de votre projet", icon="🗺️")

    pg = st.navigation(
        [page_project, page_guide, page_chat, page_roadmap],
        position="sidebar",
    )

    pg.run()
    render_sidebar_greeting()


if __name__ == "__main__":
    main()
