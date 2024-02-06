#!/usr/bin/python3
"""
Module containing the BaseModel class
"""

import uuid
from datetime import datetime
from models import storage  # Importing the storage instance

class BaseModel:
    """
    Defines the common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize instance attributes

        If kwargs is not empty:
            - Update instance attributes with the provided values.
            - Convert 'created_at' and 'updated_at' strings into datetime objects.
        Otherwise:
            - Create 'id' and 'created_at' attributes as you did previously (new instance).
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        # If kwargs is not empty, update instance attributes
        if kwargs:
            for key, value in kwargs.items():
                # Ignore __class__ as it is not an attribute of the class
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)

        # If it’s a new instance (not from a dictionary representation), add a call to the method new(self) on storage
        if not kwargs:
            storage.new(self)

    def __str__(self):
        """
        Return a string representation of the instance
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Update the public instance attribute updated_at with the current datetime
        Call save(self) method of storage
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Return a dictionary representation of the instance
        """
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict
