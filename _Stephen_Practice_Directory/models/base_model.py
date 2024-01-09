#!/usr/bin/python3

import uuid
from datetime import datetime

"""Defining a class called BaseModel which will define all common attributes/methods for other classes"""

class BaseModel:
    """The base model deinition and it's other attributes and 
    methods will follow now"""
    
    def __init__(self):
        """Initialization function that's called when a new instance
        of the class is created"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def __str__(self):
        """String printing instance method that prints the string representation of the instance """
        string = "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
        return string
    
    def save(self):
        """Public method that updates the instance of the class"""
        self.updated_at = datetime.now();
    
    def to_dict(self):
        """Public instance method that return a dictionary representation of all key/values of __dict__ of the instance 
        """
        inst_dict = self.__dict__
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = datetime.isoformat(self.created_at)
        inst_dict["updated_at"] = datetime.isoformat(self.updated_at)
        
        return inst_dict
    