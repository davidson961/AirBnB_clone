#!/usr/bin/python3


import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """FileStorage class for serializing and deserializing instances to/from JSON."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, file)

    def reload(self):
        """Deserialize the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    module_name = "models.{}".format(class_name)
                    class_ = getattr(__import__(module_name, fromlist=[class_name]), class_name)
                    instance = class_(**value)
                    self.__objects[key] = instance
        except FileNotFoundError:
            pass
