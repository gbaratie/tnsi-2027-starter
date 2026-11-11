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

## Pas à pas

Les chemins et commandes ci-dessous partent de la racine du starter. **Fourni** désigne un fichier existant ; **à créer** désigne votre travail. Les noms métier sont des exemples à adapter à votre sujet. Commencer avec des fakes, puis raccorder les services réels.

Le bouton **Consignes** et la touche **T** affichent la dernière slide : elle reste projetable pendant le travail, sans étape cachée. **Début/Home** revient à la couverture. Le [PDF](slides.pdf) conserve la même vue de travail.

### 1. Faire fonctionner ce qui est fourni

Installer `uv sync --extra rag --group dev`, puis lancer `uv run streamlit run app.py`. Avec `FILROUGE_LLM_PROVIDER=fake`, envoyer une question et constater la simulation. Lire, dans cet ordre :

1. `src/filrouge/application/ports/text_generator.py` : contrat de génération ;
2. `src/filrouge/application/use_cases/chat_with_simulation.py` : validation et délégation ;
3. `src/filrouge/adapters/adk_text_generator.py` puis `bootstrap.py` : réalisation et composition.

Choisir ensuite **un** profil live déjà décrit dans `.env.example`, compléter sa clé localement et redémarrer. Si la clé manque, l’erreur doit être visible. Ne modifier ni le port ni le domaine pour changer de fournisseur. Les concepts internes d’ADK seront étudiés en S3.

### 2. Préparer un seul document avant d’en ajouter huit

Créer un corpus public ou synthétique dans `data/sources/` avec identifiant, titre et version pour chaque document. Écrire les quatre questions de référence dans un fichier versionné. Secours : `tp/fixtures/music-library/corpus/`.

**À créer** dans `src/filrouge/domain/retrieval.py` : les types simples `Document`, `Chunk`, `RetrievedChunk`, `RagSource` et `RagReply`. Un chunk garde son ID, le document et sa version, son texte et sa position. Une réponse distingue texte, sources et abstention. Aucun import ADK ou Chroma dans ces types.

### 3. Construire l’ingestion par un test

**À créer** : contrats d’embedding et de stockage vectoriel dans `application/ports/`, puis `IngestDocuments` dans `application/use_cases/`. Capacités minimales : calculer les vecteurs d’une liste de textes, écrire/remplacer des chunks par ID et rechercher les plus proches avec limite et seuil.

Commencer avec un document, un embedding déterministe et un store en mémoire. Le test appelle deux fois l’ingestion : découpage borné, IDs stables dérivés du document/version/position, vecteurs associés au nom du modèle, pas de doublons pour la même version. Un changement de version ou de modèle exige une stratégie explicite de remplacement/réindexation.

Le fake d’embedding sert à tester le flux ; il ne prouve pas la qualité de la recherche sémantique. Chroma est une dépendance disponible, son adaptateur RAG est **à créer**. Raccorder l’adaptateur au bootstrap après le test de contrat.

### 4. Construire la réponse en commençant par l’abstention

**À créer** : `AskWithRag`, recevant embedding, vector store et le port de génération fourni. Premier test : le store retourne zéro résultat ; attendre une abstention, zéro source et **zéro appel** au générateur espion. Second test : un passage dépasse le seuil ; vérifier que le prompt contient question et passage numéroté, et que la source retournée provient exactement de ce résultat.

Puis limiter à trois passages, ajouter les citations au prompt et afficher les extraits réellement récupérés dans l’UI. Si une question connue échoue, examiner successivement le texte indexé, le modèle d’embedding, les scores et le seuil. Ne masquer aucun échec par une réponse inventée.

### 5. Terminer par la petite extraction SRP

La salutation est encore mêlée à Streamlit dans `src/filrouge/entrypoints/streamlit_app.py`. **À créer** : une fonction pure `build_greeting(name, language)` dans le domaine, testée directement ; l’UI lit les champs et affiche son résultat. Rejouer ensuite `uv run pytest` et `uv run ruff check .`.

**Démonstration** : quatre questions, sources ouvertes à l’écran, abstention, seconde ingestion sans doublon. Documenter le fournisseur, le modèle d’embedding, les paramètres de recherche et les limites observées.
