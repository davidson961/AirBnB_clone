#!/usr/bin/python3

import json
import os
import datetime

class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, mode='w', encoding='utf-8') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists; otherwise, do nothing)
        """
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as file:
                loaded_objects = json.load(file)

            for key, value in loaded_objects.items():
                class_name, obj_id = key.split('.')
                obj = eval(class_name)(**value)
                self.__objects[key] = obj

        except FileNotFoundError:
            pass
