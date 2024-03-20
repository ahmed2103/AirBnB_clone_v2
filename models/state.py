#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import (Column,String, ForeignKey)
from sqlalchemy.orm import relationship
from models.city import City
from models import eng, storage
class State(BaseModel, Base):
    """ State class mapped to be a table"""
    if eng == 'db':
        __tablename__ = 'states'

        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        cities = relationship('City', backref='state')
    else:
        name = ""


    def cities(self):
        """ Retrieve all cities that have the same id as the state"""
        all_cities = storage.all(City)
        city_list = [city for city in all_cities.values() if city.state_id == self.id]
        return city_list

