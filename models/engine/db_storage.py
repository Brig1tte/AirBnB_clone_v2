#!/usr/bin/python3

import os
import json
from models.base_model import BaseModel
from models.state import State
from models.city import City
from sqlalchemy.orm import sessionmaker


class FileStorage:
    """FileStorage class that interacts with JSON files"""

    __file_path = os.path.join(os.path.dirname(__file__), "file.json")
    __objects = {}

    @classmethod
    def all(cls, cls=None):
        """Returns all objects of the class"""
        if cls is None:
            return cls.__objects
        return {k: v for k, v in cls.__objects.items() if k.startswith(cls.__name__)}

    @classmethod
    def new(cls, obj):
        """Adds a new object to the storage"""
        cls.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    @classmethod
    def save(cls):
        """Saves all objects to the JSON file"""
        data = {k: v.to_dict() for k, v in cls.__objects.items()}
        with open(cls.__file_path, "w") as f:
            json.dump(data, f)

    @classmethod
    def delete(self, obj=None):
        Session = sessionmaker(bind=engine)
        session = Session()
        # assuming user is a User instance that you want to delete
        session.delete(user)
        # to save the changes to the database
        session.commit()
        # to release the database connection and close the session
        session.close()

    @classmethod
    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()
