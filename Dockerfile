FROM python:3.9-slim

# Installer les dépendances
RUN pip install fastapi uvicorn

# Travailler dans /app
WORKDIR /app

# Copier le fichier Python
COPY main.py /app/main.py

# Exposer le port 8000
EXPOSE 8000

# Commande pour démarrer FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
