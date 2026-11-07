# S6–S7 — Amélioration et finalisation

> Support guidé : ouvrir [`slides.html`](slides.html) dans un navigateur. Navigation avec les flèches ou la barre d'espace ; touche `E` pour modifier les textes localement.

## S6 — Choisir une amélioration

Choisir une amélioration qui sert réellement le cas d'usage : qualité du RAG, nouvelle relation du graphe, troisième tool, citations, tests ou interface. Documenter avant/après et une limite.

La capsule C5 vérifie qu'un changement de fournisseur LLM ne modifie ni le domaine ni les use cases.

## S7 — Livrer

- `uv sync` fonctionne sur une installation fraîche ;
- l'UI démarre ;
- les tests et Ruff passent ;
- `.env.example` décrit toutes les variables sans secret ;
- le corpus et le graphe sont reconstructibles ;
- les quatre questions de référence sont démontrables ;
- le README explique les limites et le démarrage ;
- chaque membre sait défendre une décision d'architecture.

La capsule C7 extrait un composant UI dupliqué dans une fonction testable.
