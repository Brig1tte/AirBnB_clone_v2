#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel

 class State(BaseModel):
     """ State class """
     __tablename__ = 'states'
     name = ""
     cities = []

     def __init__(self, *args, **kwargs):
         """Initializes a new instance of State"""
         super().__init__(*args, **kwargs)
         if kwargs:
             self.name = kwargs['name']
             del kwargs['name']

     def __repr__(self):
         """Returns a formal representation of the model"""
         return '<State: {}>'.format(self.name)
