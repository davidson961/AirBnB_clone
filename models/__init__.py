#!/usr/bin/python3
"""
Initialization module for the models package.
Creates a unique FileStorage instance and reloads it for the application.
"""

from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
