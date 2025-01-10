from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, crud
from .database import SessionLocal, engine

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
