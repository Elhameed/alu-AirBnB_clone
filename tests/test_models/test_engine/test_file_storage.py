#!/usr/bin/python3
"""Unittests for FileStorage class"""
import unittest
import os
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""

    def setUp(self):
        """Set up test environment"""
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def tearDown(self):
        """Remove test file if exists"""
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_all(self):
        """Test the all method"""
        storage.reload()
        objs = storage.all()
        self.assertIsInstance(objs, dict)

    def test_new(self):
        """Test the new method"""
        obj = BaseModel()
        storage.new(obj)
        objs = storage.all()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertTrue(key in objs)

    def test_save_reload(self):
        """Test saving and reloading objects"""
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        storage.reload()
        objs = storage.all()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertTrue(key in objs)
        reloaded_obj = objs[key]
        self.assertIsInstance(reloaded_obj, BaseModel)
        self.assertEqual(reloaded_obj.id, obj.id)

if __name__ == '__main__':
    unittest.main()

