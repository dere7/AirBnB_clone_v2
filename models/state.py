#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")

    def cities(self):
        from models import storage
        return [i for i in storage.all() if i.value().__class__ == 'City' and
                i.value().state_id == self.state_id]
