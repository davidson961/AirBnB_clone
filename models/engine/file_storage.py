#!/usr/bin/python3
"""
Module containing the FileStorage class for
serializing and deserializing instances.
"""
import json
import datetime


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        serialized_objects = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        from models.base_model import BaseModel
        try:
            with open(FileStorage.__file_path, mode='r', encoding='utf-8') as file:
                loaded_objects = json.load(file)
                for key, value in loaded_objects.items():
                    class_name = value["__class__"]
                    class_name = class_name.split('.')[-1]
                    obj_class = FileStorage.__objects.get(class_name, BaseModel)
                    obj_instance = obj_class(**value)
                    FileStorage.__objects[key] = obj_instance
        except FileNotFoundError:
            pass

    def classes(self):
        """
        Get a dictionary of class names mapped to their corresponding class objects.
        """
        from models.user import User
        return storage._FileStorage__objects
