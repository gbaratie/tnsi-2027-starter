# S3 — Agents, tools et MCP

> Support guidé : ouvrir [`slides.html`](slides.html) dans un navigateur. Navigation avec les flèches ou la barre d'espace ; touche `E` pour modifier les textes localement.

## Objectifs

1. Exposer deux capacités métier sous forme de tools validés.
2. Exécuter une boucle d'agent bornée.
3. Observer les états `completed`, `limited` et `failed`.
4. Appeler un serveur MCP local en lecture seule.

## Travail demandé

- Définir deux tools utiles au domaine du groupe : nom, description, schéma d'entrée, sortie et erreurs.
- Refuser toute requête SQL, shell ou code arbitraire proposée par le modèle.
- Borner la boucle à cinq tours par défaut.
- Arrêter la boucle après une erreur de tool au lieu de répéter indéfiniment.
- Brancher le MCP local fourni par l'enseignant et valider sa réponse avant usage.

Le jeu de secours [`../fixtures/music-library/library.json`](../fixtures/music-library/library.json) permet d'implémenter `search_library` et `get_listening_history` sans dépendance distante.

## Critères de réussite

- les entrées invalides sont rejetées avant l'appel du tool ;
- les trois états de terminaison sont couverts par les tests ;
- le nombre d'étapes apparaît dans la trace ;
- le MCP reste en lecture seule et ne reçoit aucun secret ;
- une sortie MCP est traitée comme une entrée non fiable.
