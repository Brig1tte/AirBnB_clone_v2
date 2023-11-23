#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class Amenity(BaseModel):
    name = ""

place_amenities = db.relationship('Place', secondary='place_amenity', backref=db.backref('amenities'))

    def __init__(self, name):
        """ Initialize an instance of Amenity with given name """
        super().__init__()
        self.name = name

    # A place can have many amenities
    def __init__(self, name, description, price_by_night, max_guest, number_rooms, number_bathrooms, amenity_ids):
    """ Initialize an instance of Place with given attributes """
    super().__init__()
    self.name = name
    self.description = description
    self.price_by_night = price_by_night
    self.max_guest = max_guest
    self.number_rooms = number_rooms
    self.number_bathrooms = number_bathrooms
    self.amenity_ids = amenity_ids

    @property
    def place(self):
    """ Place object that this PlaceAmenity instance is related to """
    return Place.query.filter_by(id=self.place_id).first()

    @property
    def amenity(self):
    """ Amenity object that this PlaceAmenity instance is related to """
    return Amenity.query.filter_by(id=self.amenity_id).first()

    def __init__(self, place_id, amenity_id):
    """ Initialize an instance of PlaceAmenity with given place_id and amenity_id """
    super().__init__()
    self.place_id = place_id
    self.amenity_id = amenity_id
