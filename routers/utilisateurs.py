```

### [utilisateurs.py](http://_vscodecontentref_/3)

Ce fichier contient les routes pour gérer les utilisateurs.

```python
<vscode_codeblock_uri>vscode-remote://codespaces%2Bliterate-enigma-wgxrprgj6j2gjx5/workspaces/API_SP/routers/utilisateurs.py</vscode_codeblock_uri>from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import SessionLocal

router = APIRouter(
    prefix="/utilisateurs",
    tags=["utilisateurs"],
)

# Dépendance pour obtenir la session de la base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route pour récupérer tous les utilisateurs
@router.get("/", response_model=list[schemas.Utilisateur])
def read_utilisateurs(db: Session = Depends(get_db)):
    return crud.get_utilisateurs(db)

# Route pour créer un nouvel utilisateur
@router.post("/", response_model=schemas.Utilisateur)
def create_utilisateur(utilisateur: schemas.UtilisateurCreate, db: Session = Depends(get_db)):
    return crud.create_utilisateur(db, utilisateur)

# Route pour mettre à jour un utilisateur existant
@router.put("/{utilisateur_id}", response_model=schemas.Utilisateur)
def update_utilisateur(utilisateur_id: int, utilisateur: schemas.UtilisateurUpdate, db: Session = Depends(get_db)):
    db_utilisateur = db.query(models.Utilisateur).filter(models.Utilisateur.id == utilisateur_id).first()
    if db_utilisateur is None:
        raise HTTPException(status_code=404, detail="Utilisateur not found")
    db_utilisateur.nom = utilisateur.nom
    db_utilisateur.email = utilisateur.email
    db.commit()
    db.refresh(db_utilisateur)
    return db_utilisateur

# Route pour supprimer un utilisateur
@router.delete("/{utilisateur_id}", status_code=204)
def delete_utilisateur(utilisateur_id: int, db: Session = Depends(get_db)):
    db_utilisateur = db.query(models.Utilisateur).filter(models.Utilisateur.id == utilisateur_id).first()
    if db_utilisateur is None:
        raise HTTPException(status_code=404, detail="Utilisateur not found")
    db.delete(db_utilisateur)
    db.commit()
    return