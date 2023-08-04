#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
import models
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(string(128), nullable=False)
        city = relationship("city", cascade="all, delete", backref="state")
    else:
        name = ""

        @property
        def cities(self):
            """returns a list of cities"""
            cities_objs = []
            for c in models.storage.all(City).values():
                if c.state_id == self.id:
                    cities_objs.append(c)
            return cities_objs
