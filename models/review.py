#!/usr/bin/python3
""" Review module for the HBNB project """
    
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from os import getenv



class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = 'reviews'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """ Constructor """
        super().__init__(*args, **kwargs)
