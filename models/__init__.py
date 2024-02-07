"""
Module to create a unique FileStorage instance for the application
"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
