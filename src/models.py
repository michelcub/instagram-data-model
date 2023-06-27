import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(12), nullable=False, unique=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    email = Column(String, nullable=False, unique=True)

class Follower(Base):
    __tablename__ = "follower"
    id = Column(Integer, primary_key=True)
    user_from_id = Column(ForeignKey('user.id'))
    user_to_id = Column(ForeignKey('user.id'))

class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('user.id'))

class Media(Base):
    __tablename__ = "media"
    id = Column(Integer, primary_key=True)
    post_id = Column(ForeignKey('post.id'), nullable=False)
    url = Column(String, nullable=False, nullable=False)
    type = Column(Enum("FEED", "STORY", "REEL"))

class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True)
    comment = Column(String, nullable=False)
    post_id = Column(ForeignKey('post.id'), nullable=False)
    author_id = Column(ForeignKey('user.id'), nullable=False)


def to_dict(self):
    return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
