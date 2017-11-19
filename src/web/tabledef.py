from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
 
engine = create_engine('sqlite:///labeler.db', echo=True)
Base = declarative_base()
 
########################################################################
class User(Base):
    """"""
    __tablename__ = "users"
 
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
 
    #----------------------------------------------------------------------
    def __init__(self, username, password):
        """"""
        self.username = username
        self.password = password

class Label(Base):
    __tablename__ = "user_labels"
    id = Column(Integer, primary_key=True)
    user = Column(String)
    letter = Column(String)
    description = Column(String)

    def __init__(self, user, letter, description):
        self.user = user
        self.letter = letter
        self.description = description


class Line(Base):
    __tablename__ = "line_labels"
    id = Column(Integer, primary_key=True)
    user = Column(String)
    file = Column(String)
    line = Column(Integer)
    letter = Column(String)

    def __init__(self, user, file, line, letter):
        self.user = user
        self.file = file
        self.line = line
        self.letter = letter

# create tables
Base.metadata.create_all(engine)