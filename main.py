from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
import models
from database import SessionLocal, engine
from sqlalchemy import text
from sqlalchemy.exc import OperationalError

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
        if not db.query(models.Utilisateur).first():  # Vérifier si la table est vide
            utilisateurs = [
                models.Utilisateur(nom="John Doe", email="johndoe@example.com"),
                models.Utilisateur(nom="Jane Smith", email="janesmith@example.com"),
                models.Utilisateur(nom="Alice Johnson", email="alicejohnson@example.com"),
            ]
            db.add_all(utilisateurs)
            db.commit()
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