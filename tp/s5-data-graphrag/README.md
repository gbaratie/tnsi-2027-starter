# S5 — Data Graph et GraphRAG

> Support guidé : ouvrir [`slides.html`](slides.html) dans un navigateur. Navigation avec les flèches ou la barre d'espace ; touche `E` pour modifier les textes localement.

## Objectifs

1. Projeter le domaine S4 dans un graphe sourcé et reconstructible.
2. Valider des chemins relationnels utiles.
3. Enrichir le RAG avec une traversée bornée.
4. Comparer honnêtement RAG et GraphRAG.

## Travail demandé

- Définir des IDs métier stables ; ne jamais partager les IDs internes Neo4j.
- Conserver `sourceId` et `evidence` sur les relations factuelles.
- Écrire un `graph.cypher` rejouable avec contraintes et `MERGE`.
- Valider au moins un chemin à un saut et un chemin à deux sauts.
- Résoudre les entités par ID ou alias explicite.
- Limiter la traversée à 1–2 sauts et 20 relations.
- Revenir explicitement au RAG seul si aucun chemin utile n'est trouvé.

Le fichier [`../fixtures/music-library/assertions.json`](../fixtures/music-library/assertions.json) est un jeu de secours. Il reste la source reconstructible ; Neo4j n'est qu'une projection.

## Comparaison minimale

Exécuter les mêmes quatre questions avec RAG seul et RAG + graphe :

- une question de sens ;
- une question de lien ;
- une question hybride ;
- une question hors corpus.

Une absence de gain est un résultat valable si elle est expliquée.
