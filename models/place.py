#!/usr/bin/python3
"""This module defines the Place class, which inherits from BaseModel."""
from models.base_model import BaseModel

class Place(BaseModel):
    """
    This class defines a Place with city_id, user_id, name, description,
    number_rooms, number_bathrooms, max_guest, price_by_night, latitude,
    longitude, and amenity_ids attributes.
    """
    
    def __init__(self, *args, **kwargs):
        """Initialize Place instance."""
        super().__init__(*args, **kwargs)
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
