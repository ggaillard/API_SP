from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de connexion à la base de données SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Création de l'engine SQLAlchemy
# L'option "check_same_thread" est définie sur False pour permettre l'accès à la base de données à partir de plusieurs threads
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Création de la session locale
# La session est configurée pour ne pas être autocommit et autoflush
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe de base pour les modèles SQLAlchemy
Base = declarative_base()