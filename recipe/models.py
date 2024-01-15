from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from recipe_model import Base, Recipe  # Import Base and Recipe from recipe_model
import os

db_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'recipes.db')
engine = create_engine('sqlite:///recipes.db', poolclass=NullPool, connect_args={'check_same_thread': False})

if not os.path.exists(db_file_path):
    # Create tables if not exist
    Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
