#!/usr/bin/python3


"""Write tests for the Base Model that all other classes inherits from"""
import unittest
import uuid
from datetime import datetime
from models import storage
from models.state import State


class TestState(unittest.TestCase):
    """testing for State"""
    
    def test_instantiation_State(self):
        # Test default initialization
        instance = State()
        self.assertIsInstance(instance, State)
        self.assertTrue(hasattr(instance, 'name'))