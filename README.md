# API_SP



.
├── app/
│   ├── main.py         # Code principal
│   ├── models.py       # Modèles relationnels (SQLAlchemy)
│   ├── database.py     # Connexion à SQLite
│   ├── crud.py         # Opérations CRUD
├── Dockerfile          # Conteneurisation
├── requirements.txt    # Dépendances
├── docker-compose.yml  # (Optionnel) Configuration Docker Compose
└── db.sqlite3          # Base de données SQLite (générée au runtime)
