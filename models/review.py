#!/usr/bin/python3
"""
Module containing the Review class.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that inherits from BaseModel.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize Review instance.

        Args:
            *args: Unused.
            **kwargs: Dictionary representation of the instance.
        """
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
