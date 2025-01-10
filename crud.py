from sqlalchemy.orm import Session
from models import Utilisateur, Abonnement

def get_utilisateurs(db: Session):
    return db.query(models.Utilisateur).all()

def get_abonnements(db: Session):
    return db.query(models.Abonnement).all()
