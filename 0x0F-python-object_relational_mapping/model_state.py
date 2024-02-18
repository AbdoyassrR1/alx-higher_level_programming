#!/usr/bin/python3
"""
state module
"""
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):

    """
    nherits from Base
    links to the MySQL table states
    class attribute id that represents a column of an auto-generated\
    unique integer, can’t be null and is a primary key
    class attribute name that represents a column of a string with\
    maximum 128 characters and can’t be null
    """

    __tabelname__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
