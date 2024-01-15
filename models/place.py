#!/usr/bin/python3
"""Definition of the Place Class Model
- Inheriting from the Base Model"""

from models.base_model import BaseModel
from datetime import datetime


class Place(BaseModel):
    """Place class that inherits from BaseModel"""
    
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
    
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
    #         self.city_id = ""
    #         self.user_id = ""
    #         self.name = ""
    #         self.description = ""
    #         self.number_rooms = 0
    #         self.number_bathrooms = 0
    #         self.max_guest = 0
    #         self.price_by_night = 0
    #         self.latitude = 0.0
    #         self.longitude = 0.0
    #         self.amenity_ids = []
    #         storage.new(self)
