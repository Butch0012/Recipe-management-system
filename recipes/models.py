from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

# SQLAlchemy setup
Base = declarative_base()
engine = create_engine('sqlite:///recipes.db', poolclass=NullPool, connect_args={'check_same_thread': False})


Base.metadata.create_all(engine)
print("Tables created successfully")


Session = sessionmaker(bind=engine)
session = Session()

# Recipe model
class Recipe(Base):
    __tablename__ = 'recipes'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    ingredients = Column(Text, nullable=False)
    instructions = Column(String, nullable=False)

    # Define a string representation for better display
    def __repr__(self):
        return f"<Recipe(id={self.id}, name={self.name})>"
