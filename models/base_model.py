#!/usr/bin/python3
"""This script is the base model"""

import uuid
from datetime import datetime
from models import storage  # Import the storage variable


class BaseModel:
    """BaseModel class with common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Initialize instance attributes using args and kwargs."""
        if kwargs:
            # Update attributes from the dictionary representation
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        # Convert string representation to datetime object
                        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        else:
            # Create new instance with id and created_at
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # Call the new method on storage to add the instance to __objects
            storage.new(self)

    def __str__(self):
        """Return a string representation of the instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the public instance attribute updated_at with the current datetime."""
        self.updated_at = datetime.now()
        # Call the save method on storage to serialize __objects to the JSON file
        storage.save()

    def to_dict(self):
        """
        Return a dictionary containing all keys/values of __dict__ of the instance.

        - A key __class__ is added to the dictionary with the class name of the object.
        - created_at and updated_at are converted to string objects in ISO format.
        """
        result_dict = self.__dict__.copy()
        result_dict['__class__'] = self.__class__.__name__
        result_dict['created_at'] = self.created_at.isoformat()
        result_dict['updated_at'] = self.updated_at.isoformat()
        return result_dict
