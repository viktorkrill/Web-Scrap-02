#!/usr/bin/python3
"""This module contains the class Offer"""
import models
from models.base_model import BaseModel


class Offer(BaseModel):
    """This class is inherited from BaseModel used to create Offers"""
    tittle = ""
    company = ""
    location = ""
    salary = ""
    currency = ""
