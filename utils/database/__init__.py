from config import DBSettings
import logging
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, create_engine, Index, CHAR, BOOLEAN, ARRAY
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from typing import List
from copy import deepcopy
from sqlalchemy import DDL, event

db = DBSettings()


class _Base(DeclarativeBase):

    def dict(self):
        return self.__dict__


class DBMeta(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class DataBase(metaclass=DBMeta):

    db_name: str = db.db_name

    def __init__(self):
        self.engine = create_engine(
            f"postgresql://{db.db_username}:{db.db_password}@{db.db_host}/{db.db_name}",
            echo=False)
        event.listen(_Base.metadata, 'before_create', DDL(f"CREATE SCHEMA IF NOT EXISTS {db.db_name}"))

        _Base.metadata.create_all(bind=self.engine)
        self.session = sessionmaker(bind=self.engine)()
        logging.info("DB Instance created")

