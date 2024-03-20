#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, Relationship
from models import eng

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    if eng == 'db':
        __tablename__ = 'users'
        email = Column(String(128),nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128),nullable=False)
        places = Relationship('Place', back_ref='users')
        reviews = Relationship('Review', back_ref='user')
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
