#!/usr/bin/python3
"""
Unit tests for User class
"""
import unittest
from datetime import datetime
from models.user import User
from models import storage
import os


class TestUser(unittest.TestCase):
    """Test cases for User class"""

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

    def test_user_instance_creation(self):
        """Test User instance creation"""
        user = User()

        self.assertIsInstance(user, User)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))

    def test_user_attributes(self):
        """Test User attributes"""
        user = User()
        user.email = "john.doe@example.com"
        user.password = "password"
        user.first_name = "John"
        user.last_name = "Doe"

        self.assertEqual(user.email, "john.doe@example.com")
        self.assertEqual(user.password, "password")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_user_id_generation(self):
        """Test User id generation"""
        user1 = User()
        user2 = User()

        self.assertNotEqual(user1.id, user2.id)

    def test_user_created_at_datetime(self):
        """Test User created_at is a datetime object"""
        user = User()

        self.assertIsInstance(user.created_at, datetime)

    def test_user_updated_at_datetime(self):
        """Test User updated_at is a datetime object"""
        user = User()

        self.assertIsInstance(user.updated_at, datetime)

    def test_user_save_method(self):
        """Test User save method"""
        user = User()
        old_updated_at = user.updated_at
        user.save()

        self.assertLess(old_updated_at, user.updated_at)

    def test_user_to_dict_method(self):
        """Test User to_dict method"""
        user = User()
        user.email = "john.doe@example.com"
        user.password = "password"
        user.first_name = "John"
        user.last_name = "Doe"
        user_dict = user.to_dict()

        self.assertEqual(user_dict["__class__"], "User")
        self.assertEqual(user_dict["email"], "john.doe@example.com")
        self.assertEqual(user_dict["password"], "password")
        self.assertEqual(user_dict["first_name"], "John")
        self.assertEqual(user_dict["last_name"], "Doe")
        self.assertIsInstance(user_dict["created_at"], str)
        self.assertIsInstance(user_dict["updated_at"], str)

    def test_user_str_representation(self):
        """Test User __str__ representation"""
        user = User()
        user.email = "john.doe@example.com"
        user.password = "password"
        user.first_name = "John"
        user.last_name = "Doe"
        user_str = str(user)

        self.assertIn("[User] ({})".format(user.id), user_str)
        self.assertIn("'email': 'john.doe@example.com'", user_str)
        self.assertIn("'password': 'password'", user_str)
        self.assertIn("'first_name': 'John'", user_str)
        self.assertIn("'last_name': 'Doe'", user_str)
        self.assertIn("'created_at':", user_str)
        self.assertIn("'updated_at':", user_str)

    def test_user_save_and_reload(self):
        """Test User save and reload"""
        user = User()
        user.email = "john.doe@example.com"
        user.password = "password"
        user.first_name = "John"
        user.last_name = "Doe"
        user.save()

        loaded_user = storage.all()["User.{}".format(user.id)]
        self.assertIsInstance(loaded_user, User)
        self.assertEqual(loaded_user.email, "john.doe@example.com")
        self.assertEqual(loaded_user.password, "password")
        self.assertEqual(loaded_user.first_name, "John")
        self.assertEqual(loaded_user.last_name, "Doe")


if __name__ == "__main__":
    unittest.main()
