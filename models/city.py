#!/usr/bin/python3
"""Definition of the City Class Model
- Inheriting from the Base Model"""

from models.base_model import BaseModel
from datetime import datetime


class City(BaseModel):
    """City class that inherits from BaseModel"""
    
    state_id = ""
    name = ""
    
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
    # def __init__(self, *args, **kwargs):
    #     """Initialization function that's called when a new instance
    #     of the class is created"""
    #     from models import storage

    #     if kwargs and len(kwargs) > 0:
    #         # Iterate through the dictionary and get the key/value pairs
    #         for key, value in kwargs.items():
    #             if key != "__class__":
    #                 if key == "created_at" or key == "updated_at":
    #                     setattr(self, key, datetime.fromisoformat(value))
    #                 else:
    #                     setattr(self, key, value)
    #     else:
    #         super().__init__()
    #         self.state_id = ""
    #         self.name = ""

    #         storage.new(self)
