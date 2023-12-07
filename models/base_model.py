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
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.
        If kwargs is not empty, sets attributes based on the key-value
        pairs in kwargs.
        Otherwise, initializes attributes with default values.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.fromisoformat(value)
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

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
