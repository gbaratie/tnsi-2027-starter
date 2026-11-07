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
