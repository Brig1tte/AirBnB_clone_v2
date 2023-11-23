#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel):
    """ Review classto store review information """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """ Initializes a new instance of Review """
        super().__init__(*args, **kwargs)
        if kwargs:
            self.place_id = kwargs['place_id']
            self.user_id = kwargs['user_id']
            self.text = kwargs['text']

    def __repr__(self):
        """ Returns a formal representation of the model """
        return '<Review: {}>'.format(self.place_id

class User(Base):
    """ User class to store user information """
    __tablename__ = 'users'
    id = Column(String, primary_key=True)

class Place(Base):
    """ Place class to store place information """
    __tablename__ = 'places'
    id = Column(String, primary_key=True)

class Review(Base):
    """ Review class to store review information """
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    place_id = Column(String, ForeignKey('places.id'), nullable=False)
    user_id = Column(String, ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)

    place = relationship("Place", back_populates="reviews")
    user = relationship("User", back_populates="reviews")
