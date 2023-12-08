#!/usr/bin/python
""" holds class Post"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer

DEFAULT_LENGTH = 60
DESCRIPTION_LENGTH = 128
MEDIA_LENGTH = 128

class Post(BaseModel, Base):
    """Representation of Post """
    __tablename__ = 'posts'
    user_id = Column(String(DEFAULT_LENGTH), ForeignKey('users.id'), nullable=False)
    title = Column(String(DEFAULT_LENGTH), nullable=False)
    description = Column(String(DESCRIPTION_LENGTH), nullable=False)
    media_link = Column(String(MEDIA_LENGTH), nullable=False)
    likes = Column(Integer, default=0)

    def __init__(self, *args, **kwargs):
        """initializes Post"""
        super().__init__(*args, **kwargs)
