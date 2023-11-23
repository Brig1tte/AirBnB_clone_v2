#!/usr/bin/python3
"""This module defines a class User"""
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

class User(BaseModel):
    """This class defines a user by various attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
    places = [] # Representing a relationship with the class Place

# Determine the storage type based on the environment variable
if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

# Reload the storage to ensure it is in sync with the underlying storage
storage.reload()
