"""Database configuration file."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base



SQLALCHEMY_DATABASE_URL = "sqlite:///./movie.db"

# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/dbname"
# Uncomment the above line and replace with your PostgreSQL credentials if needed.
# For SQLite, the above line is sufficient for local development.

# Créer un moteur de base de données (engine) qui établit la connexion avec notre base de données movie.db
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Définir une SessionLocal qui permet de créer des sessions pour interagir avec la base de données
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Définir une base déclarative qui permet de créer des modèles de données et qui servira de classe de base pour nos modèles SQLAlchemy
Base = declarative_base()

