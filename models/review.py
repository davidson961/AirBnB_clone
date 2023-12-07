#!/usr/bin/python3
"""
This module defines the Review class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class represents a review with attributes:
    - place_id (string): empty string (Place.id)
    - user_id (string): empty string (User.id)
    - text (string): empty string
    """
    place_id = ""
    user_id = ""
    text = ""
