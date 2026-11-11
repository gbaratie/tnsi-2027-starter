# S4 — Domaine métier et API

> Support guidé : ouvrir [`slides.html`](slides.html) dans un navigateur. Navigation avec les flèches ou la barre d'espace ; touche `E` pour modifier les textes localement.

## Objectifs

1. Construire un domaine qui parle le langage des utilisateurs.
2. Distinguer Entity, Value Object et invariant.
3. Garder le domaine indépendant de Streamlit, SQLite et FastAPI.
4. Exposer un même use case depuis l'UI et une route HTTP.

## Travail demandé

- Écrire un glossaire de 8 à 12 termes métier.
- Modéliser 2 à 4 entités et 1 à 3 Value Objects.
- Implémenter au moins deux invariants avec tests.
- Choisir un use case utile et stable.
- Créer des DTO HTTP à la frontière ; ne jamais retourner directement un objet SDK ou une exception technique.
- Ajouter une route FastAPI qui traduit la requête, appelle le use case, puis traduit la réponse.

Dans l'exemple de correction « Ma Musicothèque », le domaine contient notamment `Track`, `Artist`, `Album`, `Playlist` et `Rating`. Les groupes créent leurs propres concepts.

## Critères de réussite

- aucun import de framework ou de base de données dans `domain/` ;
- le même use case est appelé depuis l'UI et l'API ;
- les erreurs de validation deviennent des réponses HTTP explicites ;
- les tests du domaine et de l'API fonctionnent sans réseau.

## Pas à pas

Les chemins et commandes ci-dessous partent de la racine du starter. **Fourni** désigne un fichier existant ; **à créer** désigne votre travail. Les noms métier sont des exemples à adapter à votre sujet. Commencer avec des fakes, puis raccorder les services réels.

Le bouton **Consignes** et la touche **T** affichent la dernière slide : elle reste projetable pendant le travail, sans étape cachée. **Début/Home** revient à la couverture. Le [PDF](slides.pdf) conserve la même vue de travail.

### 1. Écrire une règle avec un exemple et un contre-exemple

À partir de votre glossaire, choisir une action utilisateur et deux invariants. Exemple de secours : une note entière de 1 à 5 ; une playlist sans doublon. Décrire l’entrée valide, la borne autorisée et le refus attendu avant de créer les classes.

**À créer** dans `src/filrouge/domain/` : vos entités et Value Objects, avec identifiants stables et erreurs compréhensibles. Dans `tests/test_domain_*.py`, importer directement ces types et vérifier les bornes. Lancer `uv run pytest -k domain`. Si les tests exigent Streamlit, FastAPI ou une base, déplacer cette dépendance vers un adaptateur ou une entrée.

### 2. Exécuter l’action sans interface

**À créer** dans `application/ports/` : un contrat exprimant une capacité, par exemple `MusicCatalogPort.list_tracks()`. Créer un adaptateur mémoire contenant trois objets connus, puis un use case dans `application/use_cases/`. Exemple : `SearchTracks.execute(mood, max_duration_seconds=None)`.

Tester le filtre et l’entrée invalide avec le fake. Le use case retourne des objets métier ; il ne connaît pas les codes HTTP. Brancher ensuite la même action sur une page Streamlit existante. Vérifier les mêmes paramètres que dans le test.

### 3. Ajouter une frontière HTTP fine

Installer l’extra `api` en conservant les extras déjà utiles. **À créer** : `src/filrouge/entrypoints/api.py`, avec `create_api(search_tracks)` ou une factory équivalente. Les DTO Pydantic restent dans cette entrée. La route lit les paramètres, appelle `execute` une fois et convertit chaque objet vers une réponse JSON stable. Traduire les erreurs métier vers un code choisi et documenté, par exemple 422.

Le bootstrap compose le port, son adaptateur et le use case, puis appelle la factory. Un démarrage Uvicorn suppose que vous avez réellement créé l’objet `app` ou une factory d’assemblage ; aucun module API terminé n’est fourni dans le starter initial.

### 4. Tester la route sans service distant

Dans `tests/test_api.py`, injecter le use case avec le catalogue mémoire dans la factory ; utiliser `fastapi.testclient.TestClient`. Envoyer une requête valide et vérifier statut/champs du JSON. Envoyer ensuite une entrée invalide et vérifier le code d’erreur et le message public. Ne pas démarrer un vrai serveur pour ces tests.

Si l’UI et l’API divergent, comparer d’abord les conversions d’entrée et la composition du use case. Les filtres métier ne doivent pas être recopiés dans les routes.

**Démonstration** : invariant accepté/refusé, même action UI/API et requête invalide. Documenter le chemin, les paramètres et les réponses de la route dans votre README.
