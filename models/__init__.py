#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage


# Determine the storage type based on the environment variable
if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

# Reload the storage to ensure it is in sync with the underlying storage
storage.reload()
