#!/usr/bin/python3
"""
This module defines the City class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class represents a city with attributes:
    - state_id (string): empty string (State.id)
    - name (string): empty string
    """
    state_id = ""
    name = ""
