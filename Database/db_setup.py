# db_setup.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Importing the Base from UserModel
from UserComponent.UserModel import Base

DATABASE_URL = "sqlite:///./inventory.db"  # Example SQLite DB, adjust as needed

engine = create_engine(DATABASE_URL, echo=True)

# Create all tables
def setup_db():
    Base.metadata.create_all(engine)

# Bind a session factory to the engine
Session = sessionmaker(bind=engine)

if __name__ == "__main__":
    setup_db()
