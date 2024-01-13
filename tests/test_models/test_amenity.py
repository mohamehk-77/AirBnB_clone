#!/usr/bin/python3
"""Unit test for Amenity"""
import unittest
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel


class AmenityTestCase(unittest.TestCase):
    """Class for testing Amenity"""

    def test_amenity_instance(self):
        """Test Amenity instance creation"""
        amenity = Amenity()

        # Check if amenity is an instance of both BaseModel and Amenity
        self.assertIsInstance(amenity, BaseModel)
        self.assertIsInstance(amenity, Amenity)

    def test_amenity_attributes(self):
        """Test Amenity attributes"""
        amenity = Amenity()

        # Check if attributes exist
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))
        self.assertTrue(hasattr(amenity, "name"))

        # Check the types of attributes
        self.assertIsInstance(amenity.id, str)
        self.assertIsInstance(amenity.created_at, datetime)
        self.assertIsInstance(amenity.updated_at, datetime)
        self.assertIsInstance(amenity.name, str)


if __name__ == '__main__':
    unittest.main()
