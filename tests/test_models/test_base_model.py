#!/usr/bin/python3

"""Write tests for the Base Model that all other classes inherits from"""
import unittest
import uuid
from datetime import datetime
from models import storage
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        # Clear storage before each test to ensure isolation
        storage._FileStorage__objects = {}

    def test_instantiation(self):
        # Test default initialization
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)
        self.assertTrue(hasattr(instance, 'id'))
        self.assertTrue(hasattr(instance, 'created_at'))
        self.assertTrue(hasattr(instance, 'updated_at'))

        # Test initialization with attributes
        attributes = {'name': 'Alice', 'age': 30}
        instance = BaseModel(**attributes)
        self.assertEqual(instance.name, 'Alice')
        self.assertEqual(instance.age, 30)

    def test_id_generation(self):
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_datetime_assignment(self):
        # Test assignment of datetime objects
        instance = BaseModel()
        self.assertIn("created_at", instance.to_dict())
        self.assertIn("updated_at", instance.to_dict())
        self.assertIn("id", instance.to_dict())

    def test_save(self):
        instance = BaseModel()
        initial_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(instance.updated_at, initial_updated_at)
        self.assertEqual(storage.all()[f"BaseModel.{instance.id}"], instance)

    def test_to_dict(self):
        attributes = {'name': 'Bob', 'city': 'New York', 'created_at': datetime.now().isoformat(),
                      'updated_at': datetime.now().isoformat(), 'id': str(uuid.uuid4())}
        instance = BaseModel(**attributes)
        instance_dict = instance.to_dict()
        self.assertEqual(instance_dict['__class__'], 'BaseModel')
        self.assertEqual(instance_dict['name'], 'Bob')
        self.assertEqual(instance_dict['city'], 'New York')
        self.assertTrue(isinstance(instance_dict['created_at'], str))
        self.assertTrue(isinstance(instance_dict['updated_at'], str))
    
    def test_str1(self):
        instance = BaseModel()
        expected = "[{}] ({}) {}".format(instance.__class__.__name__,
                                       instance.id, instance.__dict__)
        self.assertEqual(expected, str(instance))
        self.assertIsInstance(instance.__str__, str)
    
    # def test_str(self):
    #     instance = BaseModel()
        



if __name__ == '__main__':
    unittest.main()

