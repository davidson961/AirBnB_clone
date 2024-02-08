#!/usr/bin/python3
"""
Initialization script for the FileStorage module

This script creates an instance of the FileStorage class and reloads data from
the JSON file. The FileStorage class is responsible for serializing instances
to a JSON file and deserializing JSON files to instances.
"""

from models.engine.file_storage import FileStorage
from models.user import User

storage = FileStorage()

storage.reload()
