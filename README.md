
# API_SP

# API Utilisateurs et Abonnements

Cette application propose une API simple pour gérer deux entités : **Utilisateurs** et **Abonnements**. L'API est développée avec **FastAPI**, utilise **SQLite** comme base de données, et peut être exécutée dans un conteneur Docker.

## 📁 Structure des fichiers

```
├── main.py  # Point d'entrée de l'application
├── crud.py  # Opérations CRUD sur les bases de données
├── models.py  # Modèles SQLAlchemy représentant les tables de la base de données
├── schemas.py  # Schémas Pydantic pour la validation des données d'entrée et de sortie
├── database.py  # Configuration de la base de données SQLite
├── db.sqlite3  # Base de données SQLite
├── Dockerfile  # Configuration pour le conteneur Docker
├── requirements.txt  # Liste des dépendances
└── README.md  # Documentation du projet
```

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

### Fonctionnalités

### Fonctionnalités

- CRUD complet sur les utilisateurs et les abonnements (création, lecture, mise à jour, suppression)
- Validation des données à l'aide de Pydantic
- Documentation interactive générée automatiquement avec Swagger UI et ReDoc
- Gestion des erreurs personnalisée pour fournir des réponses claires et informatives
---
### Endpoints
```
GET /utilisateurs: Récupérer tous les utilisateurs
GET /utilisateurs/{id}: Récupérer un utilisateur spécifique
POST /utilisateurs: Créer un nouvel utilisateur
PUT /utilisateurs/{id}: Mettre à jour un utilisateur
DELETE /utilisateurs/{id}: Supprimer un utilisateur
... (endpoints similaires pour les abonnements)
```
### Développement

Structure claire et conventionnelle pour faciliter la maintenance
Tests unitaires pour assurer la qualité du code
Linting pour garantir un code propre et cohérent

### Licence
Ce projet est sous licence MIT.
