#!/usr/bin/python3
"""
Module containing the FileStorage class
"""

import os
import json
import datetime


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """
        Initializes FileStorage instance and creates an empty JSON file if it doesn't exist
        """
        try:
            with open(FileStorage.__file_path, mode='r', encoding='utf-8'):
                pass  # File exists, do nothing
        except FileNotFoundError:
            with open(FileStorage.__file_path, mode='w', encoding='utf-8') as file:
                json.dump({}, file)  # Create an empty JSON file

    def all(self):
        """
        Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as file:
            json.dump(serialized_objects, file, default=str)

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

