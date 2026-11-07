# S2 — IA, ports et premier RAG

> Support guidé : ouvrir [`slides.html`](slides.html) dans un navigateur. Navigation avec les flèches ou la barre d'espace ; touche `E` pour modifier les textes localement.

## Objectifs

1. Brancher un générateur live derrière `TextGeneratorPort` sans modifier le use case.
2. Garder le fake comme profil explicite de démonstration et de test.
3. Indexer un petit corpus TXT/Markdown.
4. Répondre avec les passages réellement récupérés et leurs sources.
5. S'abstenir lorsque le corpus ne fournit pas de preuve suffisante.

## Travail demandé

- Ajouter un adaptateur Cohere et, facultativement, Ollama.
- Choisir le fournisseur avec `FILROUGE_LLM_PROVIDER` ; une valeur inconnue doit produire une erreur de configuration.
- Définir les ports d'embedding et de recherche vectorielle nécessaires au RAG.
- Séparer `ingest` et `ask` en deux use cases.
- Limiter la taille des messages et du contexte envoyé au modèle.
- Vérifier qu'une réindexation de la même version ne crée pas de doublon.

## Corpus

Le groupe utilise en priorité son propre corpus public ou synthétique. Pour un rattrapage, les documents de [`../fixtures/music-library/corpus/`](../fixtures/music-library/corpus/) décrivent une musicothèque fictive.

## Critères de réussite

- fake et live respectent le même contrat ;
- aucun test automatique n'appelle le réseau ;
- chaque réponse RAG affiche au moins un identifiant de source et le passage récupéré ;
- une question hors corpus provoque une abstention explicite ;
- changer de modèle d'embedding invalide clairement l'ancien index.

## Capsule SRP

Extraire la génération de salutation hors de Streamlit dans une fonction pure `build_greeting()`, puis écrire les tests des langues supportées et des entrées invalides.
