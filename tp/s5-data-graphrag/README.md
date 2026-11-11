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

## Pas à pas

Les chemins et commandes ci-dessous partent de la racine du starter. **Fourni** désigne un fichier existant ; **à créer** désigne votre travail. Les noms métier sont des exemples à adapter à votre sujet. Commencer avec des fakes, puis raccorder les services réels.

Le bouton **Consignes** et la touche **T** affichent la dernière slide : elle reste projetable pendant le travail, sans étape cachée. **Début/Home** revient à la couverture. Le [PDF](slides.pdf) conserve la même vue de travail.

### 1. Réutiliser une relation du domaine S4

Préparer Neo4j/Aura et installer `uv sync --extra all --group dev`. Garder la configuration locale dans `.env`. **À créer** : une liste d’assertions JSON avec `subjectId`, `predicate`, `objectId`, `sourceId` et `evidence`. Partir d’une relation et d’un extrait que tout le groupe peut retrouver. Le secours fourni est `tp/fixtures/music-library/assertions.json`.

Garder des IDs métier stables, différents des IDs internes de Neo4j. Vérifier que chaque relation factuelle correspond à sa source avant l’import. Ajouter les autres assertions seulement après ce premier contrôle.

### 2. Créer votre procédure de reconstruction

`graph.cypher` n’est pas fourni : **à créer**, ou remplacer par votre script Python paramétré. Choisir un schéma cohérent, par exemple nœuds `Entity` avec `id`, relations `RELATED_TO` avec `kind`, `sourceId` et `evidence`. Créer la contrainte d’unicité sur `Entity.id`, puis importer avec `MERGE` et paramètres.

Importer dans une base de TP vide, noter le nombre de nœuds/relations et rejouer les mêmes assertions. Les comptes restent stables. Documenter la commande réellement utilisée et la configuration nécessaire. Ne pas effacer une base partagée pour simuler un nouveau départ.

### 3. Tester les parcours avant la génération

**À créer** : port `GraphSearch` dans `application/ports/`, fake en mémoire et adaptateur Neo4j. Préparer deux requêtes connues (un saut et deux sauts) ; paramétrer l’ID et la limite, avec un maximum de vingt relations. Chaque résultat conserve provenance et chemin.

Écrire les cas : ID connu, aucun chemin, ID inconnu et résultat sans provenance. L’alias resolver est d’abord un dictionnaire explicite nom → ID. En cas d’ambiguïté, conserver les candidats ou demander une précision ; ne pas inventer d’entité. Le modèle ne produit aucun Cypher exécuté librement.

### 4. Composer le GraphRAG et ses replis

**À créer** : `AskWithGraphRag`, réutilisant le RAG, le resolver et le port graphe. Récupérer les passages documentaires, résoudre les IDs connus puis ajouter des chemins utiles bornés au contexte. La présence d’un chemin ne remplace jamais une preuve textuelle.

Sans ID ou chemin utile : réponse du RAG seul, avec repli signalé. Sans passage documentaire suffisant : abstention. Si une relation pointe vers un document absent des preuves récupérées, ne pas la présenter comme une réponse démontrée ; enrichir la recherche de preuves ou signaler la limite. Afficher réponse, extraits et chemins réellement utilisés.

### 5. Comparer sans changer de questions

Préparer le tableau des quatre questions : sens, lien, hybride et hors corpus. Pour chaque mode, noter réponse, sources, chemin éventuel et limite. Une absence de gain est recevable si elle est expliquée. Si le résultat semble moins bon avec le graphe, inspecter aliases, provenance et taille du contexte avant de changer de modèle.

**Démonstration** : seconde reconstruction sans doublon, relation sourcée, question relationnelle et repli visible. Livrer assertions, scripts, tests, commandes et comparaison.
