#!/usr/bin/python3
"""
This script initializes an instance of the FileStorage class from the models.engine module
and reloads data from the storage file.
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
