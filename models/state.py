#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref
from models.city import City
from os import getenv
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", cascade="all, delete", backref="state")
    else:
        @property
        def cities(self):
            """returns a list of cities"""
            from models import storage
            cities_objs = []
            for c in storage.all(City).values():
                if c.state_id == self.id:
                    cities_objs.append(c)
            return cities_objs

    def close(self):
        """Deserialize JSON"""
        if getenv('HBNB_TYPE_STORAGE') == 'db':
            models.storage.close()
