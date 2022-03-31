#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        objs = FileStorage.__objects
        if cls is not None:
            objs = {k: v for k, v in FileStorage.__objects.items()
                    if v.__class__ is cls}
        return objs

    def __key(self, obj):
        """returns a key for given obj"""
        return obj.__class__.__name__ + '.' + obj.id

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__objects.update(
            {self.__key(obj): obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from .classes import classes
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """deletes obj from storage if @ obj is not
        specified does nothing"""
        if obj is not None:
            for o in FileStorage.__objects.values():
                if o is obj:
                    del FileStorage.__objects[self.__key(obj)]
                    break
