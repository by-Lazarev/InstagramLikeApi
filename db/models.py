from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship

from db.database import Base


class DbUser(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True)
    password = Column(String)

    posts = relationship("DbPost", back_populates="user")


class DbPost(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, index=True)
    image_url = Column(String)
    image_url_type = Column(String)
    caption = Column(String)
    timestamp = Column(DateTime)
    user_id = Column(Integer, ForeignKey("users.id"))

    comments = relationship("DbComment", back_populates="post")
    user = relationship("DbUser", back_populates="posts")


class DbComment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, index=True)
    text = Column(String)
    username = Column(String)
    timestamp = Column(DateTime)
    post_id = Column(Integer, ForeignKey("posts.id"))

    post = relationship("DbPost", back_populates="comments")
