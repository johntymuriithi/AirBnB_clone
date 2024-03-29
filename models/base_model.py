# Define the base model here

import uuid
from datetime import datetime

"""Defining a class called BaseModel which will define all common
attributes/methods for other classes"""


class BaseModel:
    """The base model deinition and it's other attributes and
    methods will follow now"""

    def __init__(self, *args, **kwargs):
        from models import storage
        """Initialization function that's called when a new instance
        of the class is created"""
        if kwargs and len(kwargs) > 0:
            # Iterate through the dictionary and get the key/value pairs
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """String printing instance method that prints the string
        representation of the instance """
        string = "[{}] ({}) {}".format(self.__class__.__name__,
                                       self.id, self.__dict__)
        return string

    def save(self):
        from models import storage
        """Public method that updates the instance of the class"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Public instance method that returns a dictionary representation
        of all key/values in __dict__."""
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__

        if isinstance(inst_dict["created_at"], datetime):
            inst_dict["created_at"] = datetime.isoformat(self.created_at)

        if isinstance(inst_dict["updated_at"], datetime):
            inst_dict["updated_at"] = datetime.isoformat(self.updated_at)

        return inst_dict
