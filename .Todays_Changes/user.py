from baseModels import BaseModel
from datetime import datetime
import uuid


class User(BaseModel):
    """User class that inherits from BaseModel"""
    def __init__(self, *args, **kwargs):
        from __init__ import storage
        """Initialization function that's called when a new instance
        of the class is created"""
        if kwargs and len(kwargs) > 0:
            # Iterate through the dictionary and get the key/value pairs
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or  key == "updated_at":
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
            print(self.__class__.__name__)
