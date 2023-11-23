#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from models.place import Place
from models.state import State

class City(BaseModel):
    """The city class, contains state ID and name"""
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", backref="cities", cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of City"""
        super().__init__(*args, **kwargs)
        if kwargs:
            self.state_id = kwargs['state_id']
            del kwargs['state_id']

    def __repr__(self):
        """Returns a formal representation of the model"""
        return '<City: {}>'.format(self.name)
