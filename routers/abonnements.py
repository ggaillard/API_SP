from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import SessionLocal

router = APIRouter(
    prefix="/abonnements",
    tags=["abonnements"],
)

# Dépendance pour obtenir la session de la base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route pour récupérer tous les abonnements
@router.get("/", response_model=list[schemas.Abonnement])
def read_abonnements(db: Session = Depends(get_db)):
    return crud.get_abonnements(db)

# Route pour créer un nouvel abonnement
@router.post("/", response_model=schemas.Abonnement)
def create_abonnement(abonnement: schemas.AbonnementCreate, db: Session = Depends(get_db)):
    return crud.create_abonnement(db, abonnement)

# Route pour mettre à jour un abonnement existant
@router.put("/{abonnement_id}", response_model=schemas.Abonnement)
def update_abonnement(abonnement_id: int, abonnement: schemas.AbonnementUpdate, db: Session = Depends(get_db)):
    db_abonnement = db.query(models.Abonnement).filter(models.Abonnement.id == abonnement_id).first()
    if db_abonnement is None:
        raise HTTPException(status_code=404, detail="Abonnement not found")
    db_abonnement.utilisateur_id = abonnement.utilisateur_id
    db_abonnement.service = abonnement.service
    db_abonnement.prix = abonnement.prix
    db.commit()
    db.refresh(db_abonnement)
    return db_abonnement

# Route pour supprimer un abonnement
@router.delete("/{abonnement_id}", status_code=204)
def delete_abonnement(abonnement_id: int, db: Session = Depends(get_db)):
    db_abonnement = db.query(models.Abonnement).filter(models.Abonnement.id == abonnement_id).first()
    if db_abonnement is None:
        raise HTTPException(status_code=404, detail="Abonnement not found")
    db.delete(db_abonnement)
    db.commit()
    return