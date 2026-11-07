# Parcours des TP — Starter étudiant

Ce dossier contient les points de départ nécessaires pour réaliser le projet fil rouge. Chaque groupe adapte les exemples à **son propre domaine**. La musicothèque personnelle sert uniquement de jeu de données de secours et d'exemple commun pendant les démonstrations.

| Séance | Consigne | Deck guidé | Résultat attendu |
|---|---|---|---|
| S2 | [`s2-ai-rag/`](s2-ai-rag/README.md) | [`slides.html`](s2-ai-rag/slides.html) | LLM derrière un port, premier RAG cité, abstention |
| S3 | [`s3-agents-mcp/`](s3-agents-mcp/README.md) | [`slides.html`](s3-agents-mcp/slides.html) | Deux tools, boucle bornée, MCP local en lecture seule |
| S4 | [`s4-domain-api/`](s4-domain-api/README.md) | [`slides.html`](s4-domain-api/slides.html) | Domaine pur et même use case depuis l'UI et l'API |
| S5 | [`s5-data-graphrag/`](s5-data-graphrag/README.md) | [`slides.html`](s5-data-graphrag/slides.html) | Graphe sourcé, GraphRAG borné et comparaison avec RAG |
| S6–S7 | [`s6-s7-finalisation/`](s6-s7-finalisation/README.md) | [`slides.html`](s6-s7-finalisation/slides.html) | Amélioration, intégration et livraison reproductible |

## Règles communes

- Ne jamais copier des données confidentielles de l'entreprise d'apprentissage.
- Garder un fake pour chaque dépendance distante importante.
- Ne jamais basculer silencieusement d'un mode live en mode fake.
- Versionner les scripts, métadonnées et petits jeux synthétiques ; ne pas versionner `data/`, `.env`, les index ou les secrets.
- Exécuter après chaque TP :

```bash
uv run pytest
uv run ruff check .
```

Les fichiers de `fixtures/music-library/` sont synthétiques. Ils permettent de rattraper un groupe qui n'a pas encore préparé ses propres données ; ils ne constituent pas le sujet imposé du projet.
