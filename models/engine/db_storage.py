#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from os import getenv


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """Create engine and initialize the db"""
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST", "localhost")
        database = getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(user,
                                                 password,
                                                 host,
                                                 database),
            pool_pre_ping=True
            )

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """"""
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        temp_dict = {}
        if cls:
            temp_dict = self.__session.query(cls).all()
        else:
            temp_dict = self.__session.query(User).all()
            temp_dict.extend(self.__session.query(State).all())
            temp_dict.extend(self.__session.query(City).all())
            temp_dict.extend(self.__session.query(Amenity).all())
            temp_dict.extend(self.__session.query(Place).all())
            temp_dict.extend(self.__session.query(Review).all())
        result_dict = {f"{obj.__class__.__name__}.{obj.id}": obj
                       for obj in temp_dict}

        return result_dict

    def new(self, obj):
        """Add object to the current db"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to current db"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current db"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in db and start new session"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(
            sessionmaker(bind=self.__engine,
                         expire_on_commit=False))
        self.__session = Session()
