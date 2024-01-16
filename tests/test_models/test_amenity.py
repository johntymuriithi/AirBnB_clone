#!/usr/bin/python3


"""Write tests for the Base Model that all other classes inherits from"""
import unittest
import uuid
from datetime import datetime
from models import storage
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """testing for Amenity"""
    
    def test_instantiation_Amenity(self):
        # Test default initialization
        instance = Amenity()
        self.assertIsInstance(instance, Amenity)
        self.assertTrue(hasattr(instance, 'name'))