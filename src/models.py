import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base, Mapped, mapped_column
from sqlalchemy import create_engine
from eralchemy2 import render_er
from typing import List

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id : Mapped[int] = mapped_column(primary_key=True)
    user_name = Column(String(250), unique=True, nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), unique=True, nullable=False)
    post: Mapped[List["Post"]] = relationship(back_populates="user")
    follower: Mapped[List["Follower"]] = relationship(back_populates="user")

class Post(Base):
    __tablename__ = 'post'
    id : Mapped[int] = mapped_column(primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="post")
    comment: Mapped[List["Comment"]] = relationship(back_populates="post")
    media: Mapped[List["Media"]] = relationship(back_populates="post")

    def to_dict(self):
        return {}
    
class Comment(Base):
    __tablename__ = 'comment'
    id : Mapped[int] = mapped_column(primary_key=True)
    comment_text= Column(String(250), nullable=False)
    author_id = Column(Integer, nullable=False)
    post_id : Mapped[int] = mapped_column(ForeignKey("post.id"))
    post: Mapped["Post"] = relationship(back_populates="comment")

class Follower(Base):
    __tablename__ = 'follower'
    id : Mapped[int] = mapped_column(primary_key=True)
    user_from_id : Mapped[int] = mapped_column(ForeignKey("user.id"))
    user_to_id : Mapped[int] = mapped_column(ForeignKey("user.id"))

class Media(Base):
    __tablename__ = 'media'
    id : Mapped[int] = mapped_column(primary_key=True)
    media_type = Column(String(250), nullable=False)
    url = Column(String(250), unique=True, nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))




## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
