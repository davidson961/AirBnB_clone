#!/usr/bin/python3
"""
Module containing the City class.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that inherits from BaseModel.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize City instance.

        Args:
            *args: Unused.
            **kwargs: Dictionary representation of the instance.
        """
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
