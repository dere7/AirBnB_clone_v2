#!/usr/bin/python3
""" Module for testing db storage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os
from unittest import TestCase


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'file', 'if using file skip this')
class test_DBStorage(TestCase):
    """ Class to test the fidble storage method """

    def test_db(self):
        """empty test"""
