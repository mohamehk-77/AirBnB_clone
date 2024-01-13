#!/usr/bin/python3
"""
Unit tests for City class
"""
import unittest
from datetime import datetime
from models.city import City
from models import storage
import os


class TestCity(unittest.TestCase):
    """Test cases for City class"""

    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_city_instance_creation(self):
        """Test City instance creation"""
        city = City()

        self.assertIsInstance(city, City)
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))
        self.assertTrue(hasattr(city, "state_id"))
        self.assertTrue(hasattr(city, "name"))

    def test_city_attributes(self):
        """Test City attributes"""
        city = City()
        city.state_id = "CA"
        city.name = "San Francisco"

        self.assertEqual(city.state_id, "CA")
        self.assertEqual(city.name, "San Francisco")

    def test_city_id_generation(self):
        """Test City id generation"""
        city1 = City()
        city2 = City()

        self.assertNotEqual(city1.id, city2.id)

    def test_city_created_at_datetime(self):
        """Test City created_at is a datetime object"""
        city = City()

        self.assertIsInstance(city.created_at, datetime)

    def test_city_updated_at_datetime(self):
        """Test City updated_at is a datetime object"""
        city = City()

        self.assertIsInstance(city.updated_at, datetime)

    def test_city_save_method(self):
        """Test City save method"""
        city = City()
        old_updated_at = city.updated_at
        city.save()

        self.assertLess(old_updated_at, city.updated_at)

    def test_city_to_dict_method(self):
        """Test City to_dict method"""
        city = City()
        city.state_id = "CA"
        city.name = "San Francisco"
        city_dict = city.to_dict()

        self.assertEqual(city_dict["__class__"], "City")
        self.assertEqual(city_dict["state_id"], "CA")
        self.assertEqual(city_dict["name"], "San Francisco")
        self.assertIsInstance(city_dict["created_at"], str)
        self.assertIsInstance(city_dict["updated_at"], str)

    def test_city_str_representation(self):
        """Test City __str__ representation"""
        city = City()
        city.state_id = "CA"
        city.name = "San Francisco"
        city_str = str(city)

        self.assertIn("[City] ({})".format(city.id), city_str)
        self.assertIn("'state_id': 'CA'", city_str)
        self.assertIn("'name': 'San Francisco'", city_str)
        self.assertIn("'created_at':", city_str)
        self.assertIn("'updated_at':", city_str)

    def test_city_save_and_reload(self):
        """Test City save and reload"""
        city = City()
        city.state_id = "CA"
        city.name = "San Francisco"
        city.save()

        loaded_city = storage.all()["City.{}".format(city.id)]
        self.assertIsInstance(loaded_city, City)
        self.assertEqual(loaded_city.state_id, "CA")
        self.assertEqual(loaded_city.name, "San Francisco")


if __name__ == "__main__":
    unittest.main()
