#!/usr/bin/python3


"""Write tests for the Base Model that all other classes inherits from"""
import unittest
import uuid
from datetime import datetime
from models import storage
from models.user import User


class TestUser(unittest.TestCase):
    """testing for user"""
    
    def test_instantiation_user(self):
        # Test default initialization
        instance = User()
        self.assertIsInstance(instance, User)
        self.assertTrue(hasattr(instance, 'email'))
        self.assertTrue(hasattr(instance, 'first_name'))
        self.assertTrue(hasattr(instance, 'last_name'))
        self.assertTrue(hasattr(instance, 'password'))
        