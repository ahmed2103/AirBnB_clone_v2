#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import eng
from sqlalchemy import Column, String
class Amenity(BaseModel, Base):
    """class that represent amenity model"""
    if eng == "db":
        __tablename__ = "amenities"

        name = Column(String(128), nullable=False)
    else:
        name = ""
