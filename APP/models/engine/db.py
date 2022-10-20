#!/usr/bin/python3
""" Contains the DBStorage class """

import models
from models.offer import Offer
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"Offer": Offer}


class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        HITCH_MYSQL_USER = getenv('user1')
        HITCH_MYSQL_PWD = getenv('GG8nDrzqWkP!aapgDsYrfw.p')
        HITCH_MYSQL_HOST = getenv('holberton.cm8wxkustwc4.us-east-1.rds.amazonaws.com')
        HITCH_MYSQL_DB = getenv('HITCH_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HITCH_MYSQL_USER,
                                             HITCH_MYSQL_PWD,
                                             HITCH_MYSQL_HOST,
                                             HITCH_MYSQL_DB))

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """ call remove() method on the private session attribute """
        self.__session.remove()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None

    def count(self, cls=None):
        """ count the number of objects in storage """
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())

        return
