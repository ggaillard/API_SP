# API Utilisateurs et Abonnements

Cette application FastAPI propose une API pour gérer des **Utilisateurs** et **Abonnements** avec une base de données **SQLite**. Elle est conçue pour fonctionner dans un environnement de développement **Docker**, notamment avec **GitHub Codespaces**.

#  Fonctionnalités
Gestion des utilisateurs via l'endpoint /utilisateurs.
Jeu d'essai inséré automatiquement dans la base de données SQLite.

# Étape 1: Installation et utilisation avec GitHub Codespaces
# Prérequis
- Un compte GitHub avec accès à Codespaces.
- Ce dépôt cloné sur votre compte GitHub.
# Étapes
Ouvrir Codespaces
- Cliquez sur le bouton vert `Code` dans la page du dépôt.
- Sélectionnez `Codespaces`.
- Cliquez sur `Create codespace on main`.

## 📁 Structure du projet

```
.
├──.devcontainer/   # Configuration pour Codespaces
├── main.py         # Point d'entrée de l'application (API FastAPI)
├── crud.py         # Fonctions CRUD
├── models.py       # Modèles SQLAlchemy
├── database.py     # Configuration de la base de données
├── db.sqlite3      # Base de données SQLite
├── Dockerfile      # Configuration pour le conteneur Docker
├── requirements.txt # Dépendances Python
└── README.md       # Documentation du projet
```

---

## Étape 2 :🚀 Lancer l'application

Une fois le Codespace créé, l'application est configurée pour démarrer automatiquement grâce à `.devcontainer/devcontainer.json.` 
Si ce n'est pas le cas, exécutez la commande suivante dans le terminal intégré :
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
---

### Étape 1 : Installation des dépendances
Installez les bibliothèques requises :
```bash
pip install -r requirements.txt
```
---

### Étape 3 : Tester l'API
Vous pouvez accéder à la documentation interactive de l'API via le navigateur ou un outil comme`Postman` :
- Documentation interactive Swagger : [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Endpoint utilisateurs  : [http://localhost:8000/utilisateurs](http://localhost:8000/utilisateurs

---

## Étape 4 : Utilisation de l'extension SQLite dans Visual Studio Code

## 1 : Installer l'extension SQLite
- Ouvrez Visual Studio Code.
- Allez dans l'onglet des extensions (Ctrl+Shift+X).
- Recherchez `SQLite` et installez l'extension "SQLite" de l'auteur "alexcvzz".

## 2 :Configurer une connexion
- Cliquez sur l'icône `Database` dans la barre latérale de Visual Studio Code (proposée par l'extension SQLite).
- Sélectionnez `New Connection`.
- Choisissez SQLite comme type de serveur.
- Dans le champ `Database Path`, entrez le chemin vers le fichier db.sqlite3 du projet (par défaut, ce fichier est situé à la racine du projet).
- Cliquez sur `Save` puis sur `Connect`.

 ## 3 : Explorer la base de données
- Une fois connecté, vous pourrez voir les tables et leurs données dans la base de données SQLite, y compris le jeu d'essai inséré automatiquement.
---



## 🛠 Fonctionnalités

### 1. **Endpoints disponibles**
| Endpoint             | Méthode | Description                  |
|----------------------|---------|------------------------------|
| `/utilisateurs`      | GET     | Récupérer tous les utilisateurs |
| `/abonnements`       | GET     | Récupérer tous les abonnements |

### 2. **Modèles**

#### Utilisateur
| Champ    | Type   | Description             |
|----------|--------|-------------------------|
| `id`     | int    | Identifiant unique      |
| `nom`    | string | Nom de l'utilisateur    |
| `email`  | string | Email unique            |

#### Abonnement
| Champ           | Type   | Description                    |
|------------------|--------|--------------------------------|
| `id`            | int    | Identifiant unique             |
| `utilisateur_id` | int    | Identifiant de l'utilisateur   |
| `service`        | string | Nom du service d'abonnement    |
| `prix`          | float  | Prix de l'abonnement           |

---

## 🔧 Développement

### Structure du code

1. **`main.py`** : Contient la configuration de l'application et les routes.
2. **`models.py`** : Définit les modèles SQLAlchemy pour la base de données.
3. **`crud.py`** : Contient les fonctions pour interagir avec la base de données.
4. **`database.py`** : Configure la connexion à la base de données SQLite.

---

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus d'informations.

---

