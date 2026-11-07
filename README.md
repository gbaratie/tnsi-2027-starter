# 🎓 Fil Rouge TNSI — Dauphine 2027 (Starter Kit)

Socle applicatif du projet **Transition Numérique des Systèmes d'Information (TNSI)** — Master 2 MIAGE Apprentissage, Université Paris Dauphine–PSL.

Tout au long des 7 séances (puis la soutenance S8), vous enrichissez cette application pour concevoir un **assistant métier intelligent et robuste**. Le socle fonctionne **100 % en local, sans clé API, sans compte externe ni modèle à télécharger**.

---

## ⚡ Démarrage rapide (Séance 1)

Un seul chemin d'installation : **`uv`**. Il installe lui-même la bonne version de Python (3.12) et les mêmes versions de paquets pour tout le monde, sur macOS, Linux et Windows.

### 1. Installer `uv` (une seule fois)

* **macOS / Linux :**
  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```
* **Windows (PowerShell) :**
  ```powershell
  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
  ```

Fermez puis rouvrez votre terminal et vérifiez : `uv --version`.
Autres méthodes d'installation : [docs.astral.sh/uv](https://docs.astral.sh/uv/getting-started/installation/).

### 2. Forker et cloner le projet

1. Cliquez sur **Fork** en haut à droite du dépôt GitHub.
2. Clonez **votre fork** :
   ```bash
   git clone https://github.com/<votre-compte>/tnsi-2027-starter.git
   cd tnsi-2027-starter
   ```

> Dans le dépôt public étudiant, le starter est directement à la racine. Les contributeurs du dépôt enseignant lancent les mêmes commandes depuis son dossier `starter/`.

### 3. Installer, lancer, tester

```bash
uv sync --group dev                 # installe Python 3.12 et les dépendances
uv run streamlit run app.py         # lance l'application
uv run pytest                       # lance les tests
uv run ruff check .                 # vérifie la qualité du code
```

L'application s'ouvre sur [http://localhost:8501](http://localhost:8501). Aucune activation d'environnement virtuel n'est nécessaire : `uv run` s'en charge.

### Dépendances ajoutées au fil des séances

Le démarrage S1 reste léger. Installez seulement les extras du TP courant :

```bash
uv sync --extra rag       # S2 : Chroma
uv sync --extra agent     # S3 : MCP
uv sync --extra api       # S4 : FastAPI et tests HTTP
uv sync --extra graph     # S5 : Neo4j
uv sync --extra all       # poste enseignant ou rattrapage complet
```

---

## 🎯 Mission Séance 1 : personnaliser votre vitrine

1. Ouvrez la page **🚀 Projet** dans le menu latéral.
2. Éditez `src/filrouge/entrypoints/pages/1_projet.py` dans votre éditeur :
   - **l'équipe projet** (noms et rôles) ;
   - **le problème métier** et les **utilisateurs cibles** ;
   - **les KPIs** (`st.metric`) ;
   - **le vocabulaire métier** et les **sources de données** ;
   - **au moins trois questions types**, dont une de chaque type (voir `course-authoring/docs/12_USE_CASES.md` du dépôt enseignant ou la consigne de séance).
3. Consultez **💡 Guide Streamlit** (`pages/2_guide_streamlit.py`) pour les composants disponibles.
4. Testez **💬 Interface de Chat** (`pages/3_chat.py`) : la réponse est **simulée**, aucun modèle n'est appelé.

La vitrine vit dans votre code : elle est sauvegardée par `git commit`, pas par l'application. N'y mettez ni nom d'entreprise confidentiel ni donnée sensible.

## 🧪 Parcours des TP

Le dossier [`tp/`](tp/README.md) contient les consignes, les decks guidés étape par étape, les critères de réussite et les jeux synthétiques de secours pour S2 à S7. La musicothèque fournie sert d'exemple commun ; chaque groupe conserve son propre domaine, ses mappings et ses données.

Le dossier [`skills/`](skills/README.md) accueillera progressivement les aides optionnelles destinées aux étudiants. Il est volontairement séparé des outils utilisés pour construire le cours.

---

## 🏛️ Architecture du code

Le projet applique l'**architecture hexagonale** :

```text
src/filrouge/
├── domain/            # 🧠 Règles métier pures (aucune technologie)
│   ├── chat.py        # ChatReply
│   └── exceptions.py  # ValidationError, StorageError
│
├── application/       # ⚙️ Use cases et contrats
│   ├── ports/         # TextGeneratorPort
│   └── use_cases/     # ChatWithSimulation
│
├── adapters/          # 🔌 Implémentations concrètes des ports
│   ├── fake_text_generator.py   # Simulateur de réponses, sans clé
│   └── sqlite_connection.py     # Connexion SQLite (prête pour les lots suivants, sans table)
│
├── bootstrap.py       # Assemble use cases et adaptateurs
├── config.py          # Configuration (FILROUGE_DATA_DIR)
│
└── entrypoints/       # 🖥️ Interface utilisateur
    ├── streamlit_app.py   # Navigation multipage
    └── pages/             # 1_projet, 2_guide_streamlit, 3_chat, 4_deroule
```

---

## 🔄 Rester synchronisé avec le dépôt d'origine

```bash
git remote add upstream https://github.com/gbaratie/tnsi-2027-starter.git   # une seule fois
git fetch upstream
git merge upstream/main
```

Ne versionnez jamais `.env` ni `data/` (déjà exclus par `.gitignore`). Pour une configuration locale, copiez `.env.example` en `.env`.

---

## 💡 Résolution des problèmes fréquents

* **`uv: command not found` après installation** : fermez et rouvrez le terminal ; sous Windows, vérifiez que `uv` est dans le `PATH`.
* **Le port 8501 est occupé** : `uv run streamlit run app.py --server.port 8502`.
* **Mauvaise version de Python** : ne l'installez pas à la main, `uv sync` s'en occupe. Pour la forcer : `uv python install 3.12`.
* **Réinitialiser les données locales** : supprimez le dossier `data/` s'il existe (il n'est pas créé en séance 1).
