from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models
import crud
from database import SessionLocal, engine, Base
from sqlalchemy.exc import OperationalError

def test_connection():
    try:
        # Essayer d'ouvrir une session
        db = SessionLocal()
        db.execute("SELECT 1")  # Test de la connexion
        print("Connexion réussie à la base de données.")
        db.close()
    except OperationalError as e:
        print(f"Erreur de connexion : {e}")

if __name__ == "__main__":
    test_connection()
    
# Créer les tables si elles n'existent pas
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dépendance pour la session de la base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Jeu d'essai
@app.on_event("startup")
def startup_event():
    db = SessionLocal()
    if not db.query(models.Utilisateur).first():  # Vérifie si la table est vide
        utilisateurs = [
            models.Utilisateur(nom="John Doe", email="johndoe@example.com"),
            models.Utilisateur(nom="Jane Smith", email="janesmith@example.com"),
            models.Utilisateur(nom="Alice Johnson", email="alicejohnson@example.com"),
        ]
        db.add_all(utilisateurs)
        db.commit()
    db.close()

# Endpoint pour récupérer tous les utilisateurs
@app.get("/utilisateurs")
def get_utilisateurs(db: Session = Depends(get_db)):
    return db.query(models.Utilisateur).all()

@app.get("/utilisateurs")
def read_utilisateurs(db: Session = Depends(get_db)):
    return crud.get_utilisateurs(db)

@app.get("/abonnements")
def read_abonnements(db: Session = Depends(get_db)):
    return crud.get_abonnements(db)
