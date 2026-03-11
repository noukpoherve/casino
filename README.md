# Casino Project

## Guide complet : utiliser `uv`

`uv` est un gestionnaire de paquets et d'environnements Python ultra-rapide, écrit en Rust. Il remplace `pip`, `pip-tools`, `virtualenv`, `pyenv` et bien d'autres.

---

## Installation de `uv`

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Via pip
pip install uv
```

---

## Gestion des projets

### Créer un nouveau projet

```bash
uv init mon-projet        # Crée un nouveau projet dans ./mon-projet
uv init                   # Initialise un projet dans le dossier courant
```

### Lancer le projet

```bash
uv run main.py            # Exécute un script Python dans l'environnement du projet
uv run python             # Lance un interpréteur Python interactif
uv run pytest             # Exécute une commande dans l'environnement du projet
```

---

## Gestion des dépendances

### Ajouter des paquets

```bash
uv add pandas             # Ajoute pandas au projet
uv add "requests>=2.28"   # Ajoute avec une contrainte de version
uv add --dev pytest       # Ajoute en dépendance de développement uniquement
```

### Supprimer des paquets

```bash
uv remove pandas          # Supprime pandas du projet
uv remove --dev pytest    # Supprime une dépendance de développement
```

### Installer les dépendances

```bash
uv sync                   # Installe toutes les dépendances définies dans pyproject.toml
uv sync --dev             # Installe aussi les dépendances de développement
```

### Mettre à jour les dépendances

```bash
uv lock --upgrade         # Met à jour toutes les dépendances dans le lockfile
uv lock --upgrade-package pandas  # Met à jour uniquement pandas
```

---

## Gestion de Python

### Installer une version de Python

```bash
uv python install 3.12        # Installe Python 3.12
uv python install 3.11 3.12   # Installe plusieurs versions en une commande
```

### Lister les versions disponibles

```bash
uv python list                # Liste toutes les versions Python disponibles
uv python list --installed    # Liste uniquement les versions installées
```

### Définir la version Python du projet

```bash
uv python pin 3.12            # Fixe la version Python à 3.12 pour ce projet
```

---

## Gestion de l'environnement virtuel

### Créer un environnement virtuel

```bash
uv venv                       # Crée un .venv dans le dossier courant
uv venv mon-env               # Crée un environnement nommé mon-env
uv venv --python 3.12         # Crée un environnement avec Python 3.12
```

### Activer l'environnement (sans uv)

```bash
# macOS / Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

> Avec `uv run`, il n'est pas nécessaire d'activer manuellement l'environnement.

---

## Gestion des outils globaux

### Installer un outil en global

```bash
uv tool install ruff          # Installe ruff comme outil global
uv tool install black         # Installe black comme outil global
```

### Lancer un outil sans l'installer

```bash
uvx ruff check .              # Exécute ruff sans l'installer de façon permanente
uvx black main.py             # Formate un fichier avec black
```

### Lister / supprimer les outils globaux

```bash
uv tool list                  # Liste les outils installés globalement
uv tool uninstall ruff        # Désinstalle ruff
```

---

## Lockfile

Le fichier `uv.lock` garantit que tout le monde utilise exactement les mêmes versions de paquets.

```bash
uv lock                       # Génère ou met à jour le lockfile sans installer
uv lock --check               # Vérifie que le lockfile est à jour (utile en CI)
```

---

## Commandes utiles

```bash
uv pip list                   # Liste les paquets installés dans l'environnement
uv pip show pandas            # Affiche les infos d'un paquet
uv pip freeze                 # Affiche les paquets au format requirements.txt
uv cache clean                # Vide le cache de uv
uv self update                # Met à jour uv lui-même
```

---

## Fichiers importants

| Fichier | Rôle |
|---|---|
| `pyproject.toml` | Configuration du projet et liste des dépendances |
| `uv.lock` | Versions exactes des paquets (à committer dans git) |
| `.python-version` | Version Python fixée pour le projet |
| `.venv/` | Environnement virtuel local (ne pas committer) |

---

## Exemple de workflow typique

```bash
# 1. Créer un projet
uv init casino-project
cd casino-project

# 2. Ajouter des dépendances
uv add pandas requests

# 3. Lancer le projet
uv run main.py

# 4. Ajouter un outil de dev
uv add --dev pytest

# 5. Lancer les tests
uv run pytest
```
