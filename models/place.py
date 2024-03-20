#!/usr/bin/python3
""" Place Module for HBNB project """
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models import eng, storage
from sqlalchemy import (Column, String, ForeignKey, Integer, Float, Table)
from sqlalchemy.orm import relationship
from models.review import Review

if eng == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('place.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenity.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                    primary_key=True))

class Place(BaseModel, Base):
    """class that represents Place object"""
    if eng == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'),nullable=False)
        user_id = Column(String(60), ForeignKey('user.id'),nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024),nullable=False)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship('Review', back_ref='place')
    else:
        """ A place to stay """
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    @property
    def reviews(self):
        """returns the list of Review instances with place_id equals to the
        current Place.id It will be the FileStorage relationship between Place
         and Review"""
        return [review for review in storage.all(Review).values()
                if self.id == review.place_id]

    @property
    def amenities(self):
        """returns the list of Amenity instances based on the attribute
        amenity_ids that contains all Amenity.id linked to the Place"""
        return [amen for amen in storage.all(Amenity).values()
                if self.id == amen.plaace_id]

    @amenities.setter
    def amenities(self, obj):
        """handles append method for adding an Amenity.id
            to the attribute amenity_ids
         """
        if obj is not None:
            if isinstance(obj, Amenity):
                if obj.id not in self.amenity_ids:
                    self.amenity_ids.append(obj.id)