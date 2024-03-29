#!/usr/bin/python3
"""This module defines the User class, which inherits from BaseModel."""
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
