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

## Pas à pas

Les chemins et commandes ci-dessous partent de la racine du starter. **Fourni** désigne un fichier existant ; **à créer** désigne votre travail. Les noms métier sont des exemples à adapter à votre sujet. Commencer avec des fakes, puis raccorder les services réels.

Le bouton **Consignes** et la touche **T** affichent la dernière slide : elle reste projetable pendant le travail, sans étape cachée. **Début/Home** revient à la couverture. Le [PDF](slides.pdf) conserve la même vue de travail.

### 1. Choisir une amélioration à partir d’une trace

Rejouer les quatre questions et noter un défaut réel. **À créer** : `docs/improvement.md`, contenant problème, entrée précise, résultat avant, critère attendu et limite connue. Choisir une évolution réalisable dans la séance : réglage de recherche, nouvelle relation prouvée, tool utile, validation ou parcours reproductible.

Écrire un test avec données/fakes minimaux qui échoue pour ce défaut. S’il passe déjà, votre test ne reproduit pas encore le problème. Pour une amélioration qualitative, conserver aussi les sorties et passages avant/après sur les mêmes questions.

### 2. Modifier une responsabilité et tout rejouer

Une règle va dans le domaine ; une orchestration dans le use case ; une technologie dans un adaptateur composé au bootstrap. Garder les autres paramètres stables pour attribuer le résultat à la modification. Rejouer le test ciblé, puis `uv run pytest` et `uv run ruff check .`, puis les quatre questions de référence.

Pour la capsule C5, changer de profil par configuration tout en conservant le même contrat. Pour C7, extraire seulement un composant UI réellement dupliqué et testable. La fin du projet ne demande pas une réécriture générale.

### 3. Faire installer le projet par une autre personne

Un autre membre clone dans un nouveau dossier. Il suit uniquement votre README : `uv sync --extra all --group dev`, copie locale de `.env.example`, choix du profil et commandes d’ingestion/reconstruction. Les scripts de RAG et graphe sont ceux que vous avez créés : les nommer explicitement dans le README avec leur ordre et le résultat attendu.

Ne transférer ni `.venv`, ni fichier secret, ni index ou graphe caché du premier poste. Le mode fake permet de vérifier le démarrage sans clé. Une capacité exigeant un service indisponible affiche une limite explicite ; elle ne bascule pas silencieusement en simulation.

Faire noter le premier blocage rencontré puis corriger la procédure à cet endroit. Rejouer les tests et `uv run streamlit run app.py`. L’installation n’est validée que lorsqu’un autre membre arrive au parcours annoncé sans aide orale supplémentaire.

### 4. Contrôler puis répéter

Vérifier `git status`, les fichiers suivis, les exemples de configuration et les exclusions. Les données sont publiques ou synthétiques ; les commandes reconstruisent les projections ; les limites sont écrites. Un déploiement public reste facultatif.

Répéter la démo avec un chronomètre : besoin, question simple, lien utile, garde-fou, mesure avant/après. Chaque membre explique une décision et une limite. Préparer le parcours fake comme plan B explicite, puis consigner le résultat de l’installation croisée dans le README.

**Démonstration** : même scénario avant/après, installation fraîche, sources et garde-fou visibles, défense individuelle répétée.
