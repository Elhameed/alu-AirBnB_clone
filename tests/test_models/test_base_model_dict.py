#!/usr/bin/python3
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_attributes(self):
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89

        self.assertEqual(my_model.name, "My_First_Model")
        self.assertEqual(my_model.my_number, 89)

    def test_str_method(self):
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89

        expected_str = "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), expected_str)

    def test_save_method(self):
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.save()
        new_updated_at = my_model.updated_at

        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_method(self):
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89

        obj_dict = my_model.to_dict()

        self.assertTrue('__class__' in obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertTrue('created_at' in obj_dict)
        self.assertTrue('updated_at' in obj_dict)
        self.assertTrue('id' in obj_dict)
        self.assertTrue('name' in obj_dict)
        self.assertTrue('my_number' in obj_dict)

    def test_from_dict_method(self):
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        obj_dict = my_model.to_dict()

        new_model = BaseModel.from_dict(obj_dict)

        self.assertEqual(my_model.id, new_model.id)
        self.assertEqual(my_model.name, new_model.name)
        self.assertEqual(my_model.my_number, new_model.my_number)
        self.assertEqual(my_model.created_at, new_model.created_at)
        self.assertEqual(my_model.updated_at, new_model.updated_at)
        self.assertNotEqual(my_model, new_model)

if __name__ == '__main__':
    unittest.main()
