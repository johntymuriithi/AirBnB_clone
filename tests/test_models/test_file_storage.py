#!/usr/bin/python3

# """Write tests for the file storage t"""
# import unittest
# import uuid
# from datetime import datetime
# from models import storage
# from models.base_model import BaseModel
# from models.engine.file_storage import FileStorage


# class TestFileStorage(unittest.TestCase):
#     """Defines a class TESTFIELSTORAGE"""
#     def setUp(self):
#         """Sets up all instances needed fo this test"""
#         self.baseModal = BaseModel()
#         self.storage = FileStorage()
    
#     def tearDown(self):
#         """clean up test files"""
#         FileStorage.__FileStorage__objects = {}
        
#     def test_all(self):
#         """test all method"""
#         obj = FileStorage.__FileStorage__objects
#         result = self.storage.all()
#         self.assertEqual(type(result), dict)
#         self.assertEqual(result, obj)
    
    