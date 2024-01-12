# models.py
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
import os

Base = declarative_base()
db_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'recipes.db')
engine = create_engine('sqlite:///recipes.db', poolclass=NullPool, connect_args={'check_same_thread': False})

if not os.path.exists(db_file_path):
    Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
