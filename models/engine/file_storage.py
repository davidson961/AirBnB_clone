#!/usr/bin/python3
"""
This module defines the FileStorage class that serializes instances
to a JSON file and deserializes JSON file to instances.
"""
import json
import datetime
import os


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize the __objects dictionary to a JSON file."""
        serialized = {}
        for key, value in self.__objects.items():
            class_name = key.split('.')[0]
            if class_name not in serialized:
                serialized[class_name] = []
                serialized[class_name].append(value.to_dict())
                with open(self.__file_path, 'w', encoding='utf-8') as file:
                    json.dump(serialized, file)

    def classes(self):
        """Returns a dictionary of valid classes and their references"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
                'BaseModel': BaseModel,
                'User': User,
                'State': State,
                'City': City,
                'Amenity': Amenity,
                'Place': Place,
                'Review': Review}

        return classes

    def reload(self):
        """ Deserializes the JSON file """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                try:
                    data = json.load(file)
                    for class_name, objects in data.items():
                        for obj_dict in objects:
                            obj = self.classes[class_name](**obj_dict)
                            key = "{}.{}".format(class_name, obj.id)
                            self.__objects[key] = obj
                except Exception:
                    pass
