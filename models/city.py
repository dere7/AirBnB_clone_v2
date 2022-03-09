#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from os import getenv


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'

    def __init__(self, **kwargs):
        if getenv('HBNB_TYPE_STORAGE') == 'db':
            self.name = Column(String(128), nullable=False)
            self.state_id = Column(String(60), ForeignKey(
                'states.id'), nullable=False)
        else:
            self.name = ""
            self.state_id = ""
        super().__init__(**kwargs)
