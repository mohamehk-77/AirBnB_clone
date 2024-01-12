#!/usr/bin/python3
import json

from models.base_model import BaseModel

"""Define FileStorage Class"""
class FileStorage:
    __file_path = "file.json"
    __objects = {}

    """Function to return objects"""
    def all(self):
        return self.__objects

    """Set object key"""
    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    """Serializes objects to JSON File"""
    def save(self):
        with open(self.__file_path, "w") as f:
            json.dump({key: value.to_dict() for key, value in self.__objects.items()}, f)

    def reload(self):
        try:
            with open(self.__file_path, "r") as f:
                loaded_objects = json.load(f)
            for key, value in loaded_objects.items():
                class_name = key.split('.')[0]
                cls = eval(class_name)
                self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
