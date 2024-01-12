#!/usr/bin/python3
"""
Define BaseModel class
"""
import models
import uuid
from datetime import datetime


# storage = FileStorage()
"""
Define BaseModel class
"""


class BaseModel:
    """Function to define id, date, time"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if not key == "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    """ Function that save the update date and time """
    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        Dict = self.__dict__.copy()
        Dict["__class__"] = self.__class__.__name__
        Dict["created_at"] = self.created_at.isoformat()
        Dict["updated_at"] = self.updated_at.isoformat()
        return Dict

    """Method that return class name , id, dict"""
    def __str__(self):
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
