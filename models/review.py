#!/usr/bin/python3
"""This module defines the Review class, which inherits from BaseModel."""
from models.base_model import BaseModel

class Review(BaseModel):
    """
    This class defines a Review with place_id, user_id, text attributes.
    """
    def __init__(self, *args, **kwargs):
        """Initialize Review instance."""
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
