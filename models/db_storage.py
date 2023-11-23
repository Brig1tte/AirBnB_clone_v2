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
    def reload(cls):
        """Loads all objects from the JSON file"""
        try:
            with open(cls.__file_path, "r") as f:
                data = json.load(f)
            for key, value in data.items():
                clsname, uid = key.split(".")
                if clsname == "State":
                    state = State(**value)
                    city = City(**value["cities"][0])
                    state.cities.append(city)
                    cls.__objects[key] = state
                elif clsname == "City":
                    cls.__objects[key] = City(**value)
                elif clsname == "User":
                    cls.__objects[key] = User(**value)
                elif clsname == "Place":
                    cls.__objects[key] = Place(**value)
                elif clsname == "Review":
                       cls.__ cls.__objects[objects[key]key] = Review = Place(**(**value)value)
                elif
        except FileNotFound clsname ==Error:
            pass
