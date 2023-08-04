#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
import sqlalchemy
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String


class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeingKey("states.id"), nullable=False)
