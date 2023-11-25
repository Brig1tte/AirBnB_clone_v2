#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage


class Place(BaseModel):
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
    reviews = []  # represents a relationship with the class Review


class BaseStorage:
    def reload(self):
        pass


class FileStorage(BaseStorage):
    def reload(self):
        # Implementation for reloading data from a file

    def all(self, cls):
        return super().all(cls)

    def get(self, cls, id):
        all_objects = self.all(cls)
        for obj in all_objects:
            if obj.id == id:
                return obj
        return None

    def get_reviews(self, place_id):
        return [obj for obj in self.all(Review) if obj.place_id == place_id]


class DBStorage(BaseStorage):
    def reload(self):
        # Implementation for reloading data from a database


    # Determine the storage type based on the environment variable
    if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
        storage = DBStorage()
    else:
        storage = FileStorage()

# Reload the storage to ensure it is in sync with the underlying storage
storage.reload()
