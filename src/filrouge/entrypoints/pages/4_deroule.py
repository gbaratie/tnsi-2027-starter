"""Page 4 : 🗺️ Déroulé de votre projet (Parcours & Jalons)."""

import streamlit as st

st.header("🗺️ Déroulé de votre projet — 4 Transformations, 1 Enjeu Data")
st.write(
    """
    Le programme TNSI s'articule autour de **7 séances** progressives, suivies d'une **soutenance finale (S8)**,
    pour transformer votre problème métier en un assistant intelligent complet et robuste.
    """
)

sessions = [
    ("S1", "Quatre transformations, enjeu data, lancement", "Programme de l'année, constitution des groupes, choix du sujet, fork, UI locale (C1) et vitrine du projet", True),
    (
        "S2",
        "IA, Clean Code, SOLID et premier RAG",
        (
            "Théorie IA conservée ; chat branché sur un modèle via un port et premier RAG ; théories Clean Code "
            "et SOLID, exercice C4 sur la responsabilité unique et C8 sur les ports LLM"
        ),
        False,
    ),
    (
        "S3",
        "Agents, tools et MCP",
        (
            "REX L'Oréal, stratégies IA en entreprise, agents, tools, boucle bornée et MCP ; "
            "aucune capsule d'architecture appliquée"
        ),
        False,
    ),
    (
        "S4",
        "IoT, architecture hexagonale, domaine métier et API",
        (
            "IoT et interconnexion ; théorie hexagonale ; construction du domaine métier avec C2, puis TP API C6 ; "
            "aucun TP base de données graphe"
        ),
        False,
    ),
    (
        "S5",
        "Data Management, Data Graph et GraphRAG",
        "Cours Data Management, REX Data Viz, TP Data Graph et GraphRAG ; aucun TP d'architecture",
        False,
    ),
    ("S6", "Blockchain, cloud et amélioration libre", "Blockchain et exercice « imaginer », cloud et déploiement, amélioration du projet choisie par le groupe ; capsule C5 (adaptateur de modèles)", False),
    ("S7", "Quantique, RSE, intégration et finalisation", "Flash Quantique & RSE, scénario complet, démarrage reproductible, finalisation du projet ; capsule C7 (refactoring DRY)", False),
    ("S8", "Soutenance finale", "QCM Bilan, démonstration live du parcours complet, audit d'architecture (hexagone, SOLID, Clean Code) et questions individuelles", False),
]

for code, title, desc, is_current in sessions:
    badge = "🔵 **[SÉANCE COURANTE]** " if is_current else ""
    with st.expander(f"{badge}{code} — {title}", expanded=is_current):
        st.write(desc)
