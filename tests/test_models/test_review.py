#!/usr/bin/python3


"""Write tests for the Base Model that all other classes inherits from"""
import unittest
import uuid
from datetime import datetime
from models import storage
from models.review import Review


class TestReview(unittest.TestCase):
    """testing for Review"""
    
    def test_instantiation_Review(self):
        # Test default initialization
        instance = Review()
        self.assertIsInstance(instance, Review)
        self.assertTrue(hasattr(instance, 'text'))
        self.assertTrue(hasattr(instance, 'user_id'))
        self.assertTrue(hasattr(instance, 'place_id'))