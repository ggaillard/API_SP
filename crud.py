from sqlalchemy.orm import Session
from . import models

def get_utilisateurs(db: Session):
    return db.query(models.Utilisateur).all()

def get_abonnements(db: Session):
    return db.query(models.Abonnement).all()
