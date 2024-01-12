#!/usr/bin/python3
from models.base_model import BaseModel
"""
Define User Class
"""


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
