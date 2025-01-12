from sqlalchemy.orm import Session
from app import models, schemas

# Fonction pour récupérer tous les utilisateurs
def get_utilisateurs(db: Session):
    return db.query(models.Utilisateur).all()

# Fonction pour créer un nouvel utilisateur
def create_utilisateur(db: Session, utilisateur: schemas.UtilisateurCreate):
    # Créer une instance du modèle Utilisateur
    db_utilisateur = models.Utilisateur(nom=utilisateur.nom, email=utilisateur.email)
    # Ajouter l'utilisateur à la session de la base de données
    db.add(db_utilisateur)
    # Valider la transaction
    db.commit()
    # Rafraîchir l'instance pour obtenir les données mises à jour
    db.refresh(db_utilisateur)
    return db_utilisateur

# Fonction pour récupérer tous les abonnements
def get_abonnements(db: Session):
    return db.query(models.Abonnement).all()

# Fonction pour créer un nouvel abonnement
def create_abonnement(db: Session, abonnement: schemas.AbonnementCreate):
    # Créer une instance du modèle Abonnement
    db_abonnement = models.Abonnement(utilisateur_id=abonnement.utilisateur_id, service=abonnement.service, prix=abonnement.prix)
    # Ajouter l'abonnement à la session de la base de données
    db.add(db_abonnement)
    # Valider la transaction
    db.commit()
    # Rafraîchir l'instance pour obtenir les données mises à jour
    db.refresh(db_abonnement)
    return db_abonnement

# Fonction pour mettre à jour un utilisateur existant
def update_utilisateur(db: Session, utilisateur_id: int, utilisateur: schemas.UtilisateurUpdate):
    # Récupérer l'utilisateur existant
    db_utilisateur = db.query(models.Utilisateur).filter(models.Utilisateur.id == utilisateur_id).first()
    if db_utilisateur is None:
        return None
    # Mettre à jour les champs de l'utilisateur
    db_utilisateur.nom = utilisateur.nom
    db_utilisateur.email = utilisateur.email
    # Valider la transaction
    db.commit()
    # Rafraîchir l'instance pour obtenir les données mises à jour
    db.refresh(db_utilisateur)
    return db_utilisateur

# Fonction pour supprimer un utilisateur existant
def delete_utilisateur(db: Session, utilisateur_id: int):
    # Récupérer l'utilisateur existant
    db_utilisateur = db.query(models.Utilisateur).filter(models.Utilisateur.id == utilisateur_id).first()
    if db_utilisateur is None:
        return None
    # Supprimer l'utilisateur de la session de la base de données
    db.delete(db_utilisateur)
    # Valider la transaction
    db.commit()
    return db_utilisateur

# Fonction pour mettre à jour un abonnement existant
def update_abonnement(db: Session, abonnement_id: int, abonnement: schemas.AbonnementUpdate):
    # Récupérer l'abonnement existant
    db_abonnement = db.query(models.Abonnement).filter(models.Abonnement.id == abonnement_id).first()
    if db_abonnement is None:
        return None
    # Mettre à jour les champs de l'abonnement
    db_abonnement.utilisateur_id = abonnement.utilisateur_id
    db_abonnement.service = abonnement.service
    db_abonnement.prix = abonnement.prix
    # Valider la transaction
    db.commit()
    # Rafraîchir l'instance pour obtenir les données mises à jour
    db.refresh(db_abonnement)
    return db_abonnement

# Fonction pour supprimer un abonnement existant
def delete_abonnement(db: Session, abonnement_id: int):
    # Récupérer l'abonnement existant
    db_abonnement = db.query(models.Abonnement).filter(models.Abonnement.id == abonnement_id).first()
    if db_abonnement is None:
        return None
    # Supprimer l'abonnement de la session de la base de données
    db.delete(db_abonnement)
    # Valider la transaction
    db.commit()
    return db_abonnement