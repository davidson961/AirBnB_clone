#!/usr/bin/python3
"""
This module updates the FileStorage class to manage serialization and
deserialization
of instances for all new classes: Place, State, City, Amenity, and Review.
"""

import os
import json
import datetime


class FileStorage:

    """
    This class handles serialization and deserialization of instances to
    and from a JSON file.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Provides the dictionary named "__objects."""
        return FileStorage.__objects

    def new(self, obj):
        """
        Assigns the object with the key "<object class name>.id" in
        the "__objects" set.
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes the "__objects" to a JSON file located at
        "__file_path.
        """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            res = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(res, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects.
        Only reloads if the JSON file exists.
        """
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: self.classes()[v["__class__"]](**v)
                        for k, v in obj_dict.items()}
            FileStorage.__objects = obj_dict

    def classes(self):
        """
        Provides a dictionary containing valid classes and their
        corresponding references.
        """
        from models.base_model import BaseModel

        classes = {"BaseModel": BaseModel}
        return classes
