#!/usr/bin/python3
import json


"""Define FileStorage Class"""
class FileStorage:
    __file_path = "file.json"
    __objects = {}

    """Function to return objects"""
    def all(self):
        return self.__objects

    """Set object key"""
    def new(self, obj):
        key = obj.__class__.__name__ +"." + obj.id
        self.__objects[key] = obj

    """Serializes objects to JSON File"""
    def save(self):
        with open(self.__file_path, "w") as f:
            json.dump({key: value.to_dict() for key, value in self.__objects.items()}, f)

    def reload(self):
        try:
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
        except FileNotFoundError:
            pass
