#!/usr/bin/python3
"""
Module containing the User class, a subclass of BaseModel.

The User class represents a user in the AirBnB clone project.
"""
from models.base_model import BaseModel

class User(BaseModel):
    """User class that inherits from BaseModel."""
    def __init__(self, *args, **kwargs):
        """Initialize User instance."""
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
