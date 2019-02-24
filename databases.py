from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Write your functions to interact with the database here :

def add_person(favorite_food,gender,height,age,name):
  person_object  = persons(favorite_food,gender,height,age,name)
  session.add(person_object)
  session.commit()
  return person_object
  pass

def update_product(person_id,new_fav_food, new_gender):
  person_object1=session.query(persons).filter_by(person_id=person_id).first()
  person_object1.favorite_food = new_fav_food;
  person_object1.gender = new_gender;
  session.commit()
  return person_object
  pass

def delete_product(person_id):
    session.query(persons).filter(person.person_id).delete()
    session.commit()
    pass

def get_product():
    to_get =session.query(persons).first()
    print(to_get.favorite_food+to_get.gender+to_get.height+to_get.age+to_get.name)
    return to_get
def get_all():
    return session.query(persons).all()