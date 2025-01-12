from pydantic import BaseModel

# Schéma de base pour l'utilisateur
class UtilisateurBase(BaseModel):
    nom: str
    email: str

# Schéma pour la création d'un utilisateur
class UtilisateurCreate(UtilisateurBase):
    pass

# Schéma pour la lecture d'un utilisateur
class Utilisateur(UtilisateurBase):
    id: int
    abonnements: list

    class Config:
        orm_mode = True  # Permet à Pydantic de lire les données à partir des objets ORM de SQLAlchemy

# Schéma de base pour l'abonnement
class AbonnementBase(BaseModel):
    utilisateur_id: int
    service: str
    prix: float

# Schéma pour la création d'un abonnement
class AbonnementCreate(AbonnementBase):
    pass

# Schéma pour la lecture d'un abonnement
class Abonnement(AbonnementBase):
    id: int

    class Config:
        orm_mode = True  # Permet à Pydantic de lire les données à partir des objets ORM de SQLAlchemy
