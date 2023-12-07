#!/usr/bin/python3
"""
This module defines the Amenity class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class represents an amenity with attributes:
    - name (string): empty string
    """
    name = ""
