# Diagrammes de séquence des TP

Neuf diagrammes Mermaid originaux, scénarios pédagogiques TNSI. Rendus localement avec Mermaid 12.3.0 puis intégration des fontes IBM Plex Sans (OFL, licences dans `../fonts/plex/`). SVG autonomes, sans requête ni moteur de rendu à l’exécution. Libellés français, numéros de messages, appels pleins et retours pointillés. Les ports représentent des contrats applicatifs ; une flèche ne représente pas nécessairement un appel réseau.

| Fichiers | Portée |
|---|---|
| `s2-ingestion.svg`, `s2-question.svg` | Ingestion idempotente, recherche avant génération et abstention |
| `s3-tool-guard.svg` | Proposition, contrôle, exécution et budget |
| `s4-use-case.svg`, `s4-validation.svg` | Même action pour UI/API, erreur métier traduite au HTTP |
| `s5-rebuild.svg`, `s5-question.svg` | Projection reconstructible et GraphRAG avec repli |
| `s67-regression.svg`, `s67-delivery.svg` | Test rouge/vert et installation fraîche |

Les pictogrammes inline des slides photo + explication reprennent les tracés Lucide ; licence ISC dans `../LICENSE-lucide.txt`.
