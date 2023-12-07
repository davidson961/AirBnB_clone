#!/usr/bin/python3
"""
Module containing the State class.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State class that inherits from BaseModel.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize State instance.

        Args:
            *args: Unused.
            **kwargs: Dictionary representation of the instance.
        """
        super().__init__(*args, **kwargs)
        self.name = ""
