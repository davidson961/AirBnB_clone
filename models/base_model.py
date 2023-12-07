#!/usr/bin/python3
"""
This module contains the BaseModel class.
BaseModel is the base class for all other classes in this project.
It handles initialization, serialization, and deserialization of future
instances. It includes:
- Unique ID generation for each instance using uuid
- Timestamps for creation and updates of each instance
- Methods for converting instances to a dictionary representation
"""

import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        """Initializes a new instance of the BaseModel class."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Provides a formatted string representation of the instance."""
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the 'updated_at' attribute with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance."""
        dict_rep = self.__dict__.copy()
        dict_rep["__class__"] = self.__class__.__name__
        dict_rep["created_at"] = self.created_at.isoformat()
        dict_rep["updated_at"] = self.updated_at.isoformat()
        return dict_rep
