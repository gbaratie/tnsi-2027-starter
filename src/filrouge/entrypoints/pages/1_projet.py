"""Page 1 : 🚀 Projet — Vitrine & Présentation Métier.

NOTE ÉTUDIANTS : Cette page est la vitrine interactive de votre groupe.
Vous êtes invités à la personnaliser directement dans ce fichier en Python
(textes, métriques, personas, graphiques, filtres) pour vos démonstrations et soutenances.
"""

import streamlit as st

# En-tête de la vitrine
st.title("🚀 Assistant Métier Intelligent")
st.caption("Projet Fil Rouge TNSI 2027 — Master 2 MIAGE Apprentissage, Université Paris Dauphine–PSL")

# Bannière d'introduction
st.markdown(
    """
    > 💡 **Vitrine de votre projet de semestre**  
    > Cette page constitue la présentation interactive de votre cas d'usage.  
    > Vous pouvez personnaliser directement ce fichier (`pages/1_projet.py`) avec vos propres textes, métriques et données.
    """
)

# 1. Équipe Projet
st.subheader("👥 Équipe Projet")
team_members = [
    {"nom": "Étudiant 1", "role": "Lead Architecture / Data"},
    {"nom": "Étudiant 2", "role": "Product Owner / Domaine Métier"},
    {"nom": "Étudiant 3", "role": "Ingénieur IA / RAG & Graphes"},
    {"nom": "Étudiant 4", "role": "Développeur Fullstack / Streamlit"},
]

cols_team = st.columns(len(team_members))
for i, member in enumerate(team_members):
    with cols_team[i]:
        st.markdown(
            f"""
            <div style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 12px; margin-bottom: 10px;">
                <div style="font-weight: 600; color: #1e293b;">👤 {member['nom']}</div>
                <div style="font-size: 0.85em; color: #64748b;">{member['role']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.divider()

# 2. Problème Métier et Utilisateurs Cibles
col_problem, col_kpi = st.columns([3, 2])

with col_problem:
    st.subheader("🎯 Le Problème Métier")
    st.info(
        "Décrivez ici en quelques lignes la problématique concrète que votre assistant résout pour les utilisateurs. "
        "Exemple : Les gestionnaires de sinistres passent 35% de leur temps à chercher les clauses d'exclusion dans des polices d'assurance complexes."
    )

    st.subheader("👥 Utilisateurs Cibles & Personas")
    st.markdown(
        """
        - **Gestionnaire Niveau 1 :** Besoin de réponses rapides sur les franchises courantes.
        - **Expert Sinistres :** Besoin de confronter les rapports d'expertise aux conditions contractuelles.
        """
    )

with col_kpi:
    st.subheader("📊 Valeur & KPIs Attendus")
    st.success("Gains opérationnels visés pour le métier et retour sur investissement.")

    # Exemples d'indicateurs visuels
    m1, m2 = st.columns(2)
    with m1:
        st.metric(label="Gain de temps estimé", value="-40%", delta="Objectif S2-S4")
    with m2:
        st.metric(label="Précision des réponses", value="> 90%", delta="Cible RAG")

st.divider()

# 3. Données & Questions types
col_data, col_questions = st.columns(2)

with col_data:
    st.subheader("📚 Vocabulaire Métier & Données")
    st.markdown("**Termes clés :** `Police` `Sinistre` `Franchise` `Tiers` `Exclusion` `Plafond`")
    
    st.markdown("**Sources de données identifiées :**")
    st.markdown(
        """
        - 📄 Fichiers PDF de conditions générales & particulières
        - 🗄️ Base SQL des contrats et historiques de sinistres
        - 🌐 Base de connaissances interne (FAQ, guides d'experts)
        """
    )

with col_questions:
    st.subheader("❓ Questions Types des Utilisateurs")
    st.markdown(
        """
        1. **Q1 :** *Quel est le plafond d'indemnisation pour un dégât des eaux sans franchise ?*
        2. **Q2 :** *Quelles sont les clauses d'exclusion applicables aux véhicules de prêt ?*
        3. **Q3 :** *Comment s'articule la garantie responsabilité civile avec celle du tiers identifié ?*
        """
    )
