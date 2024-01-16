#!/usr/bin/python3


"""Write tests for the Base Model that all other classes inherits from"""
import unittest
import uuid
from datetime import datetime
from models import storage
from models.city import City


class TestCity(unittest.TestCase):
    """testing for City"""
    
    def test_instantiation_City(self):
        # Test default initialization
        instance = City()
        self.assertIsInstance(instance, City)
        self.assertTrue(hasattr(instance, 'state_id'))
        self.assertTrue(hasattr(instance, 'name'))