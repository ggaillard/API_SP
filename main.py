from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models
import crud
from database import SessionLocal, engine
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

@app.get("/utilisateurs")
def read_utilisateurs(db: Session = Depends(get_db)):
    return crud.get_utilisateurs(db)

@app.get("/abonnements")
def read_abonnements(db: Session = Depends(get_db)):
    return crud.get_abonnements(db)
