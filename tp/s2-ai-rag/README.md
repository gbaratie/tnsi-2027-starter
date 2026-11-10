# S2 — IA, ports et premier RAG avec Google ADK

Support guidé : [`slides.html`](slides.html). Google ADK est déjà installé et branché dans le starter. Aujourd’hui, nous l’utilisons ; ses concepts seront expliqués en S3.

## Objectifs

1. Utiliser le même `TextGeneratorPort` en simulation, avec Cohere ou Gemini.
2. Indexer un petit corpus TXT/Markdown et séparer ingestion et question-réponse.
3. Afficher les passages récupérés et leurs sources ; s’abstenir sans preuve.
4. Conserver des tests déterministes sans réseau.

## Mise en route guidée

Depuis la racine du starter :

```bash
uv sync --extra rag --group dev
uv run streamlit run app.py
```

Le profil par défaut `fake` exécute ADK avec un modèle local simulé. Copier `.env.example` vers `.env`, puis choisir **un** profil réel et redémarrer Streamlit :

| Profil | Variables locales |
|---|---|
| Cohere | `FILROUGE_LLM_PROVIDER=cohere`, `COHERE_API_KEY`, `COHERE_MODEL=command-a-03-2025` |
| Gemini | `FILROUGE_LLM_PROVIDER=gemini`, `GOOGLE_API_KEY`, `GEMINI_MODEL=gemini-2.5-flash` |

Chaque groupe utilise sa propre clé. Une clé absente, un quota épuisé ou une panne produit une erreur explicite. Les valeurs réelles restent dans `.env`, jamais dans Git. Ollama reste facultatif.

Pour observer le parcours fourni : `uv run adk web . --host 127.0.0.1 --port 8001`, puis choisir **adk_agent**. Cette interface est un outil de développement local ; le produit reste dans Streamlit. Ne pas détailler Agent/Runner/Session aujourd’hui.

## Travail demandé

- Lire `bootstrap.py`, `adapters/adk_text_generator.py` et `adk_models.py` ; identifier où le fournisseur est choisi et où le port est réalisé.
- Vérifier que le use case de chat et l’UI ne dépendent pas des types ADK.
- Définir les ports d’embedding et de recherche vectorielle nécessaires au RAG.
- Séparer `ingest` et `ask`, limiter messages et contexte, puis appeler le générateur ADK fourni avec question et sources.
- Vérifier qu’une réindexation de la même version ne crée aucun doublon. Un changement de modèle d’embedding impose une réindexation.

ADK orchestre la génération ; il ne fabrique ni les embeddings ni les preuves. Le modèle lexical fake de la correction valide l’orchestration, pas la qualité sémantique. Un backend d’embedding réel se choisit et se mesure séparément.

## Corpus et validation

Utiliser son propre corpus public ou synthétique ; secours : [`../fixtures/music-library/corpus/`](../fixtures/music-library/corpus/).

- fake et live respectent le même contrat ; aucun test automatique n’appelle un fournisseur ;
- chaque réponse RAG affiche l’identifiant et le passage réellement récupéré ;
- une question hors corpus provoque une abstention, avant l’appel LLM ;
- le profil réel n’est jamais étiqueté « simulation » ;
- documenter le fournisseur, le modèle, les sources et les limites observées.

```bash
uv run pytest
uv run ruff check .
```

## Capsule SRP

Extraire la génération de salutation de Streamlit dans `build_greeting()`, puis tester langues et entrées invalides. Le framework ne remplace pas cette séparation des responsabilités.
