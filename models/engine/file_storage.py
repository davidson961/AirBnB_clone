#!/usr/bin/python3
"""
Module containing the FileStorage class.
"""
import os
import json


class FileStorage:
    """
    FileStorage class for serializing instances to a JSON file and deserializing JSON file to instances.
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
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        serialized_objects = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists).
        """
        from models.base_model import BaseModel
        try:
            with open(FileStorage.__file_path, mode='r', encoding='utf-8') as file:
                loaded_objects = json.load(file)
                for key, value in loaded_objects.items():
                    class_name = value["__class__"]
                    class_name = class_name.split('.')[-1]
                    obj_instance = eval(class_name)(**value)
                    FileStorage.__objects[key] = obj_instance
        except FileNotFoundError:
            pass

    def classes(self):
        """
        Get a dictionary of class names mapped to their corresponding class objects.
        """
        return storage._FileStorage__objects
