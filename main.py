from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Données en mémoire (mock)
utilisateurs = [
    {"id": 1, "nom": "Alice", "email": "alice@example.com"},
    {"id": 2, "nom": "Bob", "email": "bob@example.com"}
]

abonnements = [
    {"id": 1, "utilisateur_id": 1, "service": "Netflix", "prix": 12.99},
    {"id": 2, "utilisateur_id": 2, "service": "Spotify", "prix": 9.99}
]

# Modèles Pydantic
class Utilisateur(BaseModel):
    id: int
    nom: str
    email: str

class Abonnement(BaseModel):
    id: int
    utilisateur_id: int
    service: str
    prix: float

@app.get("/utilisateurs", response_model=List[Utilisateur])
def get_utilisateurs():
    return utilisateurs

@app.get("/abonnements", response_model=List[Abonnement])
def get_abonnements():
    return abonnements

@app.get("/docs", include_in_schema=False)
def get_documentation():
    return {"message": "Accédez à la documentation interactive via /docs"}
