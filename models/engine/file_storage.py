#!/usr/bin/python3
"""File storage module for AirBnB clone."""

import json
import os


class FileStorage:
    """Class to store and retrieve data from Console."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Function that returns all stored __objects."""

        return (self.__objects)

    def new(self, obj):
        """Function that sets __objects with class-name key."""

        class_key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[class_key] = obj

    def save(self):
        """Function that saves __objects to JSON file."""

        with open(self.__file_path, "w", encoding="utf-8") as f:
            obj = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(obj, f)

    def classes(self):
        """Function that returns dictionary of class instances"""

        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"Amenity": Amenity,
                   "BaseModel": BaseModel,
                   "City": City,
                   "Place": Place,
                   "Review": Review,
                   "User": User,
                   "State": State}
        return (classes)

    def reload(self):
        """Function that deserializes JSON file to __objects."""

        if not os.path.isfile(self.__file_path):
            return

        with open(self.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: self.classes()[v["__class__"]](**v) for
                    k, v in obj_dict.items()}
            self.__objects = obj_dict
