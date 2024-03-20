#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import (Column,String)
from sqlalchemy.orm import relationship
from models.user import eng


class City(BaseModel,Base):
    """ The city class, contains state ID and name mapped to be a table """
    if eng == 'db':
        __tablename__ = 'cities'

        name = Column(String(128),nullable=False)
        state_id = Column(String(60),nullable=False)
        places = relationship('Place',backref='cities')
    else:
        state_id = ""
        name = ""


