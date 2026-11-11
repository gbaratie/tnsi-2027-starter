# S3 — Agent Google ADK, tools et MCP

Support guidé : [`slides.html`](slides.html). Le runtime utilisé en S2 devient explicite. Une capacité locale et une recherche MCP constituent nos deux tools de référence ; chaque groupe les adapte à son domaine.

## Concepts à expliquer

| Concept | Responsabilité |
|---|---|
| `Agent` | Instructions, modèle et outils autorisés |
| `Runner` | Exécution et circulation des événements |
| `Session` / state | Contexte d’une session ; distinct du domaine et des données métier |
| `Event` | Message, proposition d’appel, résultat de tool ou réponse finale ; aucun accès au raisonnement caché |
| `FunctionTool` | Adaptation d’une fonction Python typée en outil |
| `McpToolset` | Découverte et appel d’outils via MCP, avec filtre explicite |
| Callbacks / `RunConfig` | Validation et budgets d’exécution ; la consigne seule ne les garantit pas |

## Repartir de S2

```bash
uv sync --extra agent --group dev
uv run pytest
uv run python tp/s3-agents-mcp/adk_demo/run.py
uv run adk web tp/s3-agents-mcp/adk_demo --host 127.0.0.1 --port 8001
```

L’exemple fourni permet d’observer un tool Python et un vrai serveur MCP stdio local. En profil `fake`, les décisions sont préprogrammées et signalées : ce n’est pas une démonstration de la qualité d’un LLM. Cohere et Gemini utilisent les variables déjà préparées en S2. Le modèle, le service et le tool calling restent à vérifier avant la séance.

## Travail demandé

1. Lire l’exemple `adk_demo/`, identifier Agent, modèle, tools et serveur MCP. Observer un échange complet dans ADK Web.
2. Écrire deux tools de son domaine : nom, description, entrées typées et validées, sortie structurée et erreurs. Le secours musical utilise `search_library` via MCP et `get_listening_history` en Python.
3. Garder ADK dans un adaptateur réalisant `AgentRunnerPort.execute(question) -> AgentResult`. Le use case valide la question ; ADK gère la boucle, sans imbrication avec une seconde boucle maison.
4. Ajouter la validation **avant** chaque effet, un budget de **5 appels de tools**, un budget modèle séparé et un délai global. Plusieurs tools peuvent être proposés dans un seul appel modèle : ces budgets ne sont pas interchangeables.
5. Produire `completed`, `limited` ou `failed` et une trace des tools réellement exécutés. Un tool inconnu, des arguments invalides ou un MCP indisponible arrêtent explicitement l’exécution.
6. Filtrer les tools MCP, n’envoyer aucune clé au serveur, valider ses réponses et les traiter comme des données non fiables. Aucun shell, SQL, Cypher ou code librement généré.

L’exemple public est un point de départ pour observer ADK. Le budget fin par tool, les tests des trois états et la traduction vers les objets métier font partie du travail demandé. ADK Web gère ses propres sessions locales ; le chat du starter utilise une session mémoire éphémère par question.

## Preuves de réussite

- réponse avec trace sur un scénario nominal ;
- sixième appel empêché avant son exécution ;
- tool inconnu, argument invalide, erreur modèle et sortie MCP invalide couverts ;
- budgets de temps et d’appels modèle distincts ;
- tests déterministes sans API distante et vérification du vrai protocole MCP local ;
- explication individuelle de la différence entre ADK, fournisseur LLM, tool et MCP.

```bash
uv run pytest
uv run ruff check .
```

Pour le rattrapage, les données publiques sont dans [`../fixtures/music-library/`](../fixtures/music-library/). Les modules de correction sont remis séparément par l’enseignant.

## Pas à pas

Les chemins et commandes ci-dessous partent de la racine du starter. **Fourni** désigne un fichier existant ; **à créer** désigne votre travail. Les noms métier sont des exemples à adapter à votre sujet. Commencer avec des fakes, puis raccorder les services réels.

Le bouton **Consignes** et la touche **T** affichent la dernière slide : elle reste projetable pendant le travail, sans étape cachée. **Début/Home** revient à la couverture. Le [PDF](slides.pdf) conserve la même vue de travail.

### 1. Suivre un échange fourni

Lancer les commandes de la section « Repartir de S2 ». Dans `tp/s3-agents-mcp/adk_demo/`, lire `agent.py`, `run.py`, puis `server.py`. Dans ADK Web, retrouver une proposition d’appel, le résultat du tool et la réponse finale. Rejouer d’abord en fake : ses choix préprogrammés permettent d’observer le protocole, pas d’évaluer un modèle.

### 2. Tester une fonction avant FunctionTool

Choisir une action de votre domaine en lecture seule. **À créer/adapter** : une fonction Python avec paramètres typés, description courte, validation des tailles et sortie sérialisable. Tester directement un cas valide, une entrée vide et une borne dépassée. Envelopper ensuite la fonction dans `FunctionTool` et l’ajouter à la liste d’outils autorisés.

La démonstration propose un historique local et `search_library` par MCP. Adapter les données et les noms à votre sujet. La logique métier reste indépendante d’ADK ; le tool traduit simplement ses entrées et sorties.

### 3. Garder un seul runtime

**À créer** dans `application/ports/` : `AgentRunnerPort` avec `execute(question) -> AgentResult`. Le résultat garde statut, réponse et étapes (nom du tool, arguments et sortie). Un use case valide la question ; l’adaptateur ADK exécute la boucle. Le bootstrap injecte cet adaptateur. Ne pas ajouter une autre boucle d’agent autour du Runner.

### 4. Contrôler avant chaque effet

Dans les callbacks de l’adaptateur, vérifier le nom du tool et ses arguments, puis réserver le budget **avant** d’appeler la capacité métier. Une invocation du modèle peut proposer plusieurs tools : compter chacun des appels effectivement autorisés.

**À créer** : un modèle de test qui propose six tools. Le résultat doit être `limited`, avec au plus cinq effets métier. Ajouter séparément un test du maximum de six appels modèle et un test du délai global de trente secondes. Utiliser un faux appel lent ou une horloge contrôlée pour ne pas ralentir toute la suite. La limite `max_llm_calls` seule ne garantit pas le budget par tool.

### 5. Éprouver la frontière MCP

Le serveur stdio fourni se lance depuis la démo ; lire sa commande avant d’en créer un autre. Conserver un `tool_filter` explicite, transmettre seulement les données nécessaires et valider la forme/tailles des résultats reçus. Ne transmettre aucune clé de fournisseur au serveur.

Tester une réponse mal formée et un serveur absent : l’adaptateur produit `failed` avec une erreur publique, sans relancer silencieusement en fake. Si le nominal ne fonctionne pas, examiner la découverte des tools, le nom autorisé et le schéma reçu avant de changer le prompt.

**Démonstration** : nominal `completed`, argument refusé, budget `limited` et erreur MCP `failed`. Montrer les échanges exécutés ; une trace n’est pas un accès au raisonnement caché du modèle.
