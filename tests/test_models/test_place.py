#!/usr/bin/python3
"""
Unit tests for Place class
"""
import unittest
from datetime import datetime
from models.place import Place
from models import storage
import os


class TestPlace(unittest.TestCase):
    """Test cases for Place class"""

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

    def test_place_instance_creation(self):
        """Test Place instance creation"""
        place = Place()

        self.assertIsInstance(place, Place)
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))
        self.assertTrue(hasattr(place, "city_id"))
        self.assertTrue(hasattr(place, "user_id"))
        self.assertTrue(hasattr(place, "name"))
        self.assertTrue(hasattr(place, "description"))
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertTrue(hasattr(place, "latitude"))
        self.assertTrue(hasattr(place, "longitude"))
        self.assertTrue(hasattr(place, "amenity_ids"))

    def test_place_attributes(self):
        """Test Place attributes"""
        place = Place()
        place.city_id = "123"
        place.user_id = "456"
        place.name = "Luxury Apartment"
        place.description = "A beautiful place to stay"
        place.number_rooms = 3
        place.number_bathrooms = 2
        place.max_guest = 6
        place.price_by_night = 150
        place.latitude = 37.7749
        place.longitude = -122.4194
        place.amenity_ids = ["wifi", "pool", "parking"]

        self.assertEqual(place.city_id, "123")
        self.assertEqual(place.user_id, "456")
        self.assertEqual(place.name, "Luxury Apartment")
        self.assertEqual(place.description, "A beautiful place to stay")
        self.assertEqual(place.number_rooms, 3)
        self.assertEqual(place.number_bathrooms, 2)
        self.assertEqual(place.max_guest, 6)
        self.assertEqual(place.price_by_night, 150)
        self.assertEqual(place.latitude, 37.7749)
        self.assertEqual(place.longitude, -122.4194)
        self.assertEqual(place.amenity_ids, ["wifi", "pool", "parking"])

    def test_place_id_generation(self):
        """Test Place id generation"""
        place1 = Place()
        place2 = Place()

        self.assertNotEqual(place1.id, place2.id)

    def test_place_created_at_datetime(self):
        """Test Place created_at is a datetime object"""
        place = Place()

        self.assertIsInstance(place.created_at, datetime)

    def test_place_updated_at_datetime(self):
        """Test Place updated_at is a datetime object"""
        place = Place()

        self.assertIsInstance(place.updated_at, datetime)

    def test_place_save_method(self):
        """Test Place save method"""
        place = Place()
        old_updated_at = place.updated_at
        place.save()

        self.assertLess(old_updated_at, place.updated_at)

    def test_place_to_dict_method(self):
        """Test Place to_dict method"""
        place = Place()
        place.city_id = "123"
        place.user_id = "456"
        place.name = "Luxury Apartment"
        place.description = "A beautiful place to stay"
        place.number_rooms = 3
        place.number_bathrooms = 2
        place.max_guest = 6
        place.price_by_night = 150
        place.latitude = 37.7749
        place.longitude = -122.4194
        place.amenity_ids = ["wifi", "pool", "parking"]
        place_dict = place.to_dict()

        self.assertEqual(place_dict["__class__"], "Place")
        self.assertEqual(place_dict["city_id"], "123")
        self.assertEqual(place_dict["user_id"], "456")
        self.assertEqual(place_dict["name"], "Luxury Apartment")
        self.assertEqual(place_dict["description"],
                         "A beautiful place to stay")
        self.assertEqual(place_dict["number_rooms"], 3)
        self.assertEqual(place_dict["number_bathrooms"], 2)
        self.assertEqual(place_dict["max_guest"], 6)
        self.assertEqual(place_dict["price_by_night"], 150)
        self.assertEqual(place_dict["latitude"], 37.7749)
        self.assertEqual(place_dict["longitude"], -122.4194)
        self.assertEqual(place_dict["amenity_ids"], [
                         "wifi", "pool", "parking"])
        self.assertIsInstance(place_dict["created_at"], str)
        self.assertIsInstance(place_dict["updated_at"], str)

    def test_place_str_representation(self):
        """Test Place __str__ representation"""
        place = Place()
        place.city_id = "123"
        place.user_id = "456"
        place.name = "Luxury Apartment"
        place.description = "A beautiful place to stay"
        place.number_rooms = 3
        place.number_bathrooms = 2
        place.max_guest = 6
        place.price_by_night = 150
        place.latitude = 37.7749
        place.longitude = -122.4194
        place.amenity_ids = ["wifi", "pool", "parking"]
        place_str = str(place)

        self.assertIn("[Place] ({})".format(place.id), place_str)
        self.assertIn("'city_id': '123'", place_str)
        self.assertIn("'user_id': '456'", place_str)
        self.assertIn("'name': 'Luxury Apartment'", place_str)
        self.assertIn("'description': 'A beautiful place to stay'", place_str)
        self.assertIn("'number_rooms': 3", place_str)
        self.assertIn("'number_bathrooms': 2", place_str)
        self.assertIn("'max_guest': 6", place_str)
        self.assertIn("'price_by_night': 150", place_str)
        self.assertIn("'latitude': 37.7749", place_str)
        self.assertIn("'longitude': -122.4194", place_str)
        self.assertIn("'amenity_ids': ['wifi', 'pool', 'parking']", place_str)
        self.assertIn("'created_at':", place_str)
        self.assertIn("'updated_at':", place_str)

    def test_place_save_and_reload(self):
        """Test Place save and reload"""
        place = Place()
        place.city_id = "123"
        place.user_id = "456"
        place.name = "Luxury Apartment"
        place.description = "A beautiful place to stay"
        place.number_rooms = 3
        place.number_bathrooms = 2
        place.max_guest = 6
        place.price_by_night = 150
        place.latitude = 37.7749
        place.longitude = -122.4194
        place.amenity_ids = ["wifi", "pool", "parking"]
        place.save()

        loaded_place = storage.all()["Place.{}".format(place.id)]
        self.assertIsInstance(loaded_place, Place)
        self.assertEqual(loaded_place.city_id, "123")
        self.assertEqual(loaded_place.user_id, "456")
        self.assertEqual(loaded_place.name, "Luxury Apartment")
        self.assertEqual(loaded_place.description, "A beautiful place to stay")
        self.assertEqual(loaded_place.number_rooms, 3)
        self.assertEqual(loaded_place.number_bathrooms, 2)
        self.assertEqual(loaded_place.max_guest, 6)
        self.assertEqual(loaded_place.price_by_night, 150)
        self.assertEqual(loaded_place.latitude, 37.7749)
        self.assertEqual(loaded_place.longitude, -122.4194)
        self.assertEqual(loaded_place.amenity_ids, ["wifi", "pool", "parking"])


if __name__ == "__main__":
    unittest.main()
