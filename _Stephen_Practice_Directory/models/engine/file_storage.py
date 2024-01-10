#!/usr/bin/python3

"""Creating a Class called File Storage:
This will be use for the process of serialization and deserialization """

import json
import os
from datetime import datetime

class FileStorage:
    """The File Storage class that will have attributes and methods used for JSON dumps and loads of instance to and from dict to string to file"""
    __file_path = "file.json"
    __objects = {}
    
    def __init__(self):
        """The init function that is called when an object is being instantiated from the class"""
        pass
    
    def all(self):
        """Returns the dictionary - the public class attribute"""
        return self.__objects
    
    def new(self, obj):
        """Sets in the __object diction the objec with key <obj class name.id"""
    
        # self.__objects = {**self.__objects, f"{obj.__class__.__name__}.{obj.id}": obj}
        # self.__objects.obj.__class__ = obj
        # obj.created_at = datetime.isoformat(obj.created_at)
        # obj.updated_at = datetime.isoformat(obj.updated_at)
        
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj
    
    def save(self):
        """Serializes __objects to the JSON file in path: __file_path"""

        serializable_objects = {}
        
        for key, obj in self.__objects.items():
            serializable_objects[key] = obj.to_dict()
        
        serialized = json.dumps(serializable_objects)
        
        # Open a file on the file path in the public class attribute and write the serialized string to it
        try:
            with open(self.__file_path, "w") as file:
                file.write(serialized)
        except Exception:
            pass
        
    def reload(self):
        """Deserializes the JSON file to __objects """
        if os.path.exists(self.__file_path):
            # means it exists 
            deserialized = json.loads(self.__file_path)
            self.__objects = deserialized
    
    
    