"""Page 2 : 💡 Guide Streamlit — Architecture, Composants & Bonnes Pratiques."""

import streamlit as st

st.header("💡 Guide Streamlit — Architecture, Composants & Bonnes Pratiques")
st.write(
    """
    Ce guide pédagogique détaille l'organisation de l'interface graphique du projet,
    illustre **tous les composants graphiques utilisés sur la page Projet**,
    explique le fonctionnement du Chat et rappelle les bonnes pratiques d'architecture logicielle.
    """
)

# Liens vers la documentation officielle
st.info(
    """
    📚 **Ressources & Documentation Officielle Streamlit :**
    - 🌐 **Documentation générale :** [docs.streamlit.io](https://docs.streamlit.io)
    - ⚡ **Aide-mémoire (Cheat Sheet) :** [docs.streamlit.io/develop/quick-reference/cheat-sheet](https://docs.streamlit.io/develop/quick-reference/cheat-sheet)
    - 💬 **Composants de Chat IA :** [docs.streamlit.io/develop/api-reference/chat](https://docs.streamlit.io/develop/api-reference/chat)
    - 🗺️ **Navigation Multipage (`st.navigation`) :** [docs.streamlit.io/develop/concepts/multipage-apps/page-and-navigation](https://docs.streamlit.io/develop/concepts/multipage-apps/page-and-navigation)
    """
)

st.divider()

# =============================================================================
# 1. ARCHITECTURE & ORGANISATION DES PAGES
# =============================================================================

st.subheader("📁 1. Architecture & Organisation des Pages")
st.markdown(
    """
    L'interface graphique est isolée dans la couche **`src/filrouge/entrypoints/`** de l'Architecture Hexagonale.  
    Toutes les vues de l'application sont découpées en fichiers modulaires :
    """
)

st.code(
    """starter/
├── app.py                                # Lanceur racine (appelle streamlit_app.main)
└── src/filrouge/entrypoints/
    ├── streamlit_app.py                  # Point d'entrée UI (déclare st.navigation)
    └── pages/                            # 📄 VUES MODULAIRES STREAMLIT
        ├── 1_projet.py                   # 👈 MODIFIEZ ICI : Vitrine, équipe et problème métier
        ├── 2_guide_streamlit.py          # Ce guide interactif
        ├── 3_chat.py                     # 👈 MODIFIEZ ICI : Interface de conversation
        └── 4_deroule.py                  # Calendrier des séances du projet (S1 à S8)""",
    language="text",
)

st.markdown("#### ➕ Comment ajouter une nouvelle page à votre projet ?")
st.markdown(
    """
    1. **Créez un nouveau fichier Python** dans `src/filrouge/entrypoints/pages/` (ex: `5_analyse.py`).
    2. **Déclarez la page** dans `src/filrouge/entrypoints/streamlit_app.py` en ajoutant une ligne `st.Page` :
    """
)
st.code(
    """# Dans src/filrouge/entrypoints/streamlit_app.py :
page_analyse = st.Page(str(pages_dir / "5_analyse.py"), title="Analyse de Données", icon="📊")

pg = st.navigation(
    [page_project, page_guide, page_chat, page_roadmap, page_analyse], # ← Ajout ici
    position="sidebar",
)""",
    language="python",
)

st.divider()

# =============================================================================
# 2. TOUS LES COMPOSANTS UTILISÉS SUR LA PAGE PROJET (Visuel + Code)
# =============================================================================

st.subheader("🎨 2. Galerie des Composants de la Page Projet")
st.write("Retrouvez ci-dessous **l'ensemble des composants graphiques** utilisés pour bâtir votre vitrine métier :")

# --- A. Titres, Sous-titres et Légendes ---
st.markdown("#### A. Titres & Textes Formatés (`st.title`, `st.caption`, `st.subheader`, `st.markdown`)")
col_txt_vis, col_txt_code = st.columns([1, 1])
with col_txt_vis:
    st.caption("🖥️ **Rendu visuel :**")
    st.markdown("### 🚀 Titre de Section (`st.markdown`)")
    st.caption("Sous-titre ou métadonnée atténuée (`st.caption`)")
    st.markdown("> 💡 **Bannière de mise en avant** avec blockquote (`st.markdown`)")
with col_txt_code:
    st.caption("💻 **Code Python :**")
    st.code(
        """st.title("🚀 Titre Principal")
st.caption("Sous-titre ou métadonnée")
st.subheader("Titre de section")
st.markdown("> 💡 **Bannière Markdown** avec blockquote")""",
        language="python",
    )

st.markdown("---")

# --- B. Cartes HTML / CSS Personnalisées (Cartes Équipe) ---
st.markdown("#### B. Cartes Stylées HTML/CSS (`st.markdown(..., unsafe_allow_html=True)`)")
col_html_vis, col_html_code = st.columns([1, 1])
with col_html_vis:
    st.caption("🖥️ **Rendu visuel :**")
    st.markdown(
        """
        <div style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 12px;">
            <div style="font-weight: 600; color: #1e293b;">👤 Nom de l'Étudiant</div>
            <div style="font-size: 0.85em; color: #64748b;">Rôle / Spécialité Métier</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with col_html_code:
    st.caption("💻 **Code Python :**")
    st.code(
        """st.markdown(
    \"\"\"
    <div style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 12px;">
        <div style="font-weight: 600; color: #1e293b;">👤 Nom de l'Étudiant</div>
        <div style="font-size: 0.85em; color: #64748b;">Rôle / Spécialité</div>
    </div>
    \"\"\",
    unsafe_allow_html=True,
)""",
        language="python",
    )

st.markdown("---")

# --- C. Découpage en Colonnes & Séparateurs ---
st.markdown("#### C. Colonnes & Séparateurs (`st.columns`, `st.divider`)")
col_col_vis, col_col_code = st.columns([1, 1])
with col_col_vis:
    st.caption("🖥️ **Rendu visuel :**")
    c_gauche, c_droite = st.columns([3, 2])
    with c_gauche:
        st.write("Colonne gauche (largeur 3)")
    with c_droite:
        st.write("Colonne droite (largeur 2)")
    st.divider()
    st.caption("Ligne de séparation (`st.divider()`) ci-dessus")
with col_col_code:
    st.caption("💻 **Code Python :**")
    st.code(
        """# Colonnes avec ratios de largeur personnalisés :
col_gauche, col_droite = st.columns([3, 2])
with col_gauche:
    st.write("Contenu gauche...")
with col_droite:
    st.write("Contenu droit...")

st.divider() # Ligne de séparation horizontale""",
        language="python",
    )

st.markdown("---")

# --- D. Encadrés d'Information, Succès et Alerte ---
st.markdown("#### D. Encadrés de Statut (`st.info`, `st.success`, `st.warning`)")
col_box_vis, col_box_code = st.columns([1, 1])
with col_box_vis:
    st.caption("🖥️ **Rendu visuel :**")
    st.info("ℹ️ `st.info` : Présentation du problème métier.")
    st.success("✅ `st.success` : Valeur et gains opérationnels attendus.")
    st.warning("⚠️ `st.warning` : Point d'attention ou prérequis.")
with col_box_code:
    st.caption("💻 **Code Python :**")
    st.code(
        """st.info("ℹ️ Présentation du problème métier")
st.success("✅ Valeur et ROI attendus")
st.warning("⚠️ Point d'attention")""",
        language="python",
    )

st.markdown("---")

# --- E. Indicateurs Métier & KPIs ---
st.markdown("#### E. Indicateurs Métier & KPIs (`st.metric`)")
col_kpi_vis, col_kpi_code = st.columns([1, 1])
with col_kpi_vis:
    st.caption("🖥️ **Rendu visuel :**")
    m1, m2 = st.columns(2)
    m1.metric(label="Gain de temps", value="-40%", delta="Objectif S2-S4")
    m2.metric(label="Précision RAG", value="> 90%", delta="Cible")
with col_kpi_code:
    st.caption("💻 **Code Python :**")
    st.code(
        """col1, col2 = st.columns(2)
col1.metric(label="Gain de temps", value="-40%", delta="Objectif S2-S4")
col2.metric(label="Précision RAG", value="> 90%", delta="Cible")""",
        language="python",
    )

st.divider()

# =============================================================================
# 3. FONCTIONNEMENT DU CHAT IA
# =============================================================================

st.subheader("💬 3. Fonctionnement de l'Interface de Chat")
st.markdown(
    """
    Le chat repose sur 3 mécanismes fondamentaux de Streamlit combinés à l'architecture hexagonale :
    
    1. **Mémorisation dans `st.session_state`** : Streamlit ré-exécutant le script à chaque message, les échanges sont stockés dans `st.session_state["chat_history"]`.
    2. **Affichage stylé avec `st.chat_message`** : Permet de distinguer les bulles de l'utilisateur (`user`) et de l'assistant (`assistant`).
    3. **Délégation au Use Case** : L'interface ne génère aucune réponse elle-même ; elle appelle `app.chat_with_simulation.execute(prompt)` qui dialogue avec le port de génération.
    """
)

st.code(
    """# Exemple type du mécanisme de chat utilisé dans pages/3_chat.py :
import streamlit as st

# 1. Initialisation de l'historique dans la session
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# 2. Ré-affichage des messages précédents
for sender, message, is_sim in st.session_state["chat_history"]:
    with st.chat_message(sender):
        if is_sim:
            st.caption("⚙️ Réponse simulée")
        st.markdown(message)

# 3. Zone de saisie
user_prompt = st.chat_input("Posez votre question...")
if user_prompt:
    # Affiche et enregistre le message utilisateur
    st.session_state["chat_history"].append(("user", user_prompt, False))
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # Appel au Use Case hexagonal (Lot 0 : Fake / Lot 1 : Cohere, Ollama)
    reply = app.chat_with_simulation.execute(user_prompt)
    
    # Affiche et enregistre la réponse de l'assistant
    st.session_state["chat_history"].append(("assistant", reply.text, reply.is_simulation))
    with st.chat_message("assistant"):
        st.markdown(reply.text)""",
    language="python",
)

st.divider()

# =============================================================================
# 4. STRUCTURE DU CODE & BONNES PRATIQUES HEXAGONALES
# =============================================================================

st.subheader("🏛️ 4. Structure du Code & Bonnes Pratiques")
st.markdown(
    """
    ### 🔄 Le Cycle de Vie Streamlit (*Top-to-Bottom*)
    - À chaque clic ou saisie utilisateur, Streamlit ré-exécute le script Python depuis la première ligne.
    - Toute variable locale est réinitialisée sauf si elle est persistée dans **`st.session_state`**.
    
    ### 📐 Règle d'or : L'UI délègue aux Use Cases
    - **Aucune requête SQL brute ni appel SDK direct dans les pages `pages/*.py`.**
    - L'interface se contente de capturer les entrées utilisateur, d'appeler un use case (`app.<nom_use_case>.execute()`) et de mettre en forme le résultat.
    - Cela permet de tester 100% de votre logique métier avec `pytest` ou `unittest` sans jamais avoir besoin d'ouvrir un navigateur !
    """
)
