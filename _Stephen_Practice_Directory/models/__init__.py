"""Just a place to instantiate file storage"""
from .engine.file_storage import FileStorage

storage = FileStorage()

storage.reload()
