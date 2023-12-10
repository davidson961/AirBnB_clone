#!/usr/bin/python3
"""
Module defining the FileStorage class.
"""
import datetime
import json
import os


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes
    JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            s = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(s, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists).
        Otherwise, do nothing.
        """
        from models.base_model import BaseModel
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
            obj_dict = json.load(file)
            obj_dict = {k: BaseModel(**v) for k, v in obj_dict.items()}
            FileStorage.__objects = obj_dict

    def valid_classes(cls):
        """
        Returns a list of valid class names.
        """
        return [name for name in cls.__objects.keys()]
