#!/usr/bin/python3
"""
Module containing the Amenity class.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class that inherits from BaseModel.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize Amenity instance.

        Args:
            *args: Unused.
            **kwargs: Dictionary representation of the instance.
        """
        super().__init__(*args, **kwargs)
        self.name = ""
