# API Utilisateurs et Abonnements

Cette application propose une API simple pour gérer deux entités : **Utilisateurs** et **Abonnements**. L'API est développée avec **FastAPI**, utilise **SQLite** comme base de données, et peut être exécutée dans un conteneur Docker.

## 📁 Structure des fichiers

```
.
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

## 🚀 Lancer l'application

### Prérequis
- **Python 3.9+** installé
- **pip** pour gérer les dépendances
- (Optionnel) **Docker** pour exécuter l'application dans un conteneur

---

### Étape 1 : Installation des dépendances
Installez les bibliothèques requises :
```bash
pip install -r requirements.txt
```

---

### Étape 2 : Lancer l'application localement
Exécutez le fichier `main.py` :
```bash
uvicorn main:app --reload
```

L'API sera disponible à l'adresse [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

### Étape 3 : Tester l'API
Vous pouvez accéder à la documentation interactive de l'API via :
- Swagger UI : [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc : [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🐳 Utiliser Docker

### Étape 1 : Construire l'image Docker
Construisez l'image à partir du fichier `Dockerfile` :
```bash
docker build -t api-utilisateurs-abonnements .
```

---

### Étape 2 : Lancer le conteneur
Exécutez le conteneur :
```bash
docker run -d -p 8000:8000 api-utilisateurs-abonnements
```

L'API sera disponible à l'adresse [http://127.0.0.1:8000](http://127.0.0.1:8000).



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

