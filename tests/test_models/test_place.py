#!/usr/bin/python3


"""Write tests for the Base Model that all other classes inherits from"""
import unittest
import uuid
from datetime import datetime
from models import storage
from models.place import Place


class TestPlace(unittest.TestCase):
    """testing for Place"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
    def test_instantiation_Place(self):
        # Test default initialization
        instance = Place()
        self.assertIsInstance(instance, Place)
        self.assertTrue(hasattr(instance, 'name'))
        self.assertTrue(hasattr(instance, 'city_id'))
        self.assertTrue(hasattr(instance, 'user_id'))
        self.assertTrue(hasattr(instance, 'description'))
        self.assertTrue(hasattr(instance, 'number_rooms'))
        self.assertTrue(hasattr(instance, 'number_bathrooms'))
        self.assertTrue(hasattr(instance, 'max_guest'))
        self.assertTrue(hasattr(instance, 'price_by_night'))
        self.assertTrue(hasattr(instance, 'latitude'))
        self.assertTrue(hasattr(instance, 'amenity_ids'))
        self.assertTrue(hasattr(instance, 'longitude'))