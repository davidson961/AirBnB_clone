#!/usr/bin/python3
"""
Module to initialize the models package.
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
