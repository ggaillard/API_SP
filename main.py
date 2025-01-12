from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
import models
from database import SessionLocal, engine
from sqlalchemy import text
from sqlalchemy.exc import OperationalError
import os

# Fonction pour tester la connexion à la base de données
def test_connection():
    try:
        # Essayer d'ouvrir une connexion
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))  # Tester la connexion
            print("Successfully connected to the database.")
    except OperationalError as e:
        print(f"Connection error: {e}")

# Fonction de démarrage pour initialiser la base de données
def startup():
    # Créer les tables si elles n'existent pas
    print("Creating tables if they do not exist...")
    models.Base.metadata.create_all(bind=engine)
    print("Tables created successfully.")
    
    # Ajouter des données initiales si nécessaire
    db = SessionLocal()
    try:
        # Vérifier si les tables sont vides
        if not db.query(models.Utilisateur).first() and not db.query(models.Abonnement).first():
            # Exécuter le script SQL pour insérer les données initiales
            with engine.connect() as connection:
                with open(os.path.join(os.path.dirname(__file__), 'seed.sql'), 'r') as file:
                    sql_script = file.read()
                connection.execute(text(sql_script))
                print("Seed data inserted successfully.")
    except Exception as e:
        print(f"Error seeding data: {e}")
    finally:
        db.close()

# Appeler la fonction de démarrage
startup()

# Création de l'application FastAPI
app = FastAPI()

# Gestionnaire d'exceptions global
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": f"Internal Server Error: {exc}"}
    )

# Dépendance pour la session de la base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Inclusion des routeurs pour les utilisateurs et les abonnements
from app.routers import utilisateurs, abonnements

app.include_router(utilisateurs.router)
app.include_router(abonnements.router)

# Endpoint racine
@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}