from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base

# Définition du modèle Utilisateur
class Utilisateur(Base):
    __tablename__ = "utilisateurs"

    # Identifiant unique de l'utilisateur
    id = Column(Integer, primary_key=True, index=True)
    # Nom de l'utilisateur
    nom = Column(String, index=True)
    # Email unique de l'utilisateur
    email = Column(String, unique=True, index=True)

    # Relation avec les abonnements
    abonnements = relationship("Abonnement", back_populates="utilisateur")

# Définition du modèle Abonnement
class Abonnement(Base):
    __tablename__ = "abonnements"

    # Identifiant unique de l'abonnement
    id = Column(Integer, primary_key=True, index=True)
    # Clé étrangère référant à l'identifiant de l'utilisateur
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    # Nom du service auquel l'utilisateur est abonné
    service = Column(String, index=True)
    # Prix de l'abonnement
    prix = Column(Float)

    # Relation avec l'utilisateur
    utilisateur = relationship("Utilisateur", back_populates="abonnements")