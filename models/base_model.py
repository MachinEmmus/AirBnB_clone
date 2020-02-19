#!/usr/bin/python3

"""
Class BaseModel defines all common attributes/methods for other classes
"""

from datetime import datetime
import models
import uuid


class BaseModel():
    """Class BaseModel"""
    def __init__(self, *args, **kwargs):
        """Function that instance a new object"""
        if (len(kwargs) > 0):
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value,
                            "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def save(self):
        """Updates update_at and call storage save method"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
            Change type of values to isoformat, and return a dictionary
            with all keys/values of the isntance
        """
        ans = self.__dict__.copy()
        ans.update({'__class__': self.__class__.__name__})
        ans['created_at'] = ans['created_at'].isoformat()
        ans['updated_at'] = ans['updated_at'].isoformat()
        return ans

    def __str__(self):
        """Overwrite __str__ method"""
        return "[" + self.__class__.__name__ + "] (" + self.id + ") " +\
               str(self.__dict__)
