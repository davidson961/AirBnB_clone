#!/usr/bin/python3
"""
Module containing the FileStorage class
"""

import json

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
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
<<<<<<< HEAD
        FileStorage.__objects[key] = obj
=======
        self.__objects[key] = obj
>>>>>>> c4f3c940ed5ad9986288f568a18be87fc0274159

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        serialized_objects = {}
<<<<<<< HEAD
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as file:
            json.dump(serialized_objects, file, default=str)
=======
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, mode='w', encoding='utf-8') as file:
            json.dump(serialized_objects, file)
>>>>>>> c4f3c940ed5ad9986288f568a18be87fc0274159

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists; otherwise, do nothing)
        """
        try:
<<<<<<< HEAD
            with open(FileStorage.__file_path, mode='r', encoding='utf-8') as file:
                loaded_objects = json.load(file)

            for key, value in loaded_objects.items():
                class_name, obj_id = key.split('.')
                obj = eval(class_name)(**value)
                FileStorage.__objects[key] = obj

        except FileNotFoundError:
            pass

=======
            with open(self.__file_path, mode='r', encoding='utf-8') as file:
                loaded_objects = json.load(file)

            for key, value in loaded_objects.items():
                class_name, obj_id = key.split('.')
                obj = eval(class_name)(**value)
                self.__objects[key] = obj

        except FileNotFoundError:
            pass
>>>>>>> c4f3c940ed5ad9986288f568a18be87fc0274159
