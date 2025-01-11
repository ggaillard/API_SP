from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
import models
import crud
from database import SessionLocal, engine
from sqlalchemy import text
from sqlalchemy.exc import OperationalError

def test_connection():
    try:
        # Try to open a connection
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))  # Test the connection
            print("Successfully connected to the database.")
    except OperationalError as e:
        print(f"Connection error: {e}")

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur votre API FastAPI !"}

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": f"Internal Server Error: {exc}"}
    )

# Dependency for the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Seed data
@app.on_event("startup")
def startup_event():
    # Create tables if they do not exist
    print("Creating tables if they do not exist...")
    models.Base.metadata.create_all(bind=engine)
    print("Tables created successfully.")
    
    db = SessionLocal()
    try:
        if not db.query(models.Utilisateur).first():  # Check if the table is empty
            utilisateurs = [
                models.Utilisateur(nom="John Doe", email="johndoe@example.com"),
                models.Utilisateur(nom="Jane Smith", email="janesmith@example.com"),
                models.Utilisateur(nom="Alice Johnson", email="alicejohnson@example.com"),
            ]
            db.add_all(utilisateurs)
            db.commit()
    except Exception as e:
        print(f"Error seeding data: {e}")
    finally:
        db.close()

# Endpoint to get all users
@app.get("/utilisateurs")
def read_utilisateurs(db: Session = Depends(get_db)):
    return crud.get_utilisateurs(db)

# Endpoint to get all subscriptions
@app.get("/abonnements")
def read_abonnements(db: Session = Depends(get_db)):
    return crud.get_abonnements(db)