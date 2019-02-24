from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :
class person(Base):
    __tablename__ = 'persons'
	person_id = Column(Integer ,  primary_key = True , autoincrement=True)
	name = Column(String)
	age = Column(Integer)
	height = Column(Integer)
	gender = Column(String)
	favorite_food = Column(String)
    pass
