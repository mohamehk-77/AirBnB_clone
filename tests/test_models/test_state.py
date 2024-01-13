#!/usr/bin/python3
"""
Unit tests for State class
"""
import unittest
from datetime import datetime
from models.state import State
from models import storage
import os


class TestState(unittest.TestCase):
    """Test cases for State class"""

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

    def test_state_instance_creation(self):
        """Test State instance creation"""
        state = State()

        self.assertIsInstance(state, State)
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))
        self.assertTrue(hasattr(state, "name"))

    def test_state_attributes(self):
        """Test State attributes"""
        state = State()
        state.name = "California"

        self.assertEqual(state.name, "California")

    def test_state_id_generation(self):
        """Test State id generation"""
        state1 = State()
        state2 = State()

        self.assertNotEqual(state1.id, state2.id)

    def test_state_created_at_datetime(self):
        """Test State created_at is a datetime object"""
        state = State()

        self.assertIsInstance(state.created_at, datetime)

    def test_state_updated_at_datetime(self):
        """Test State updated_at is a datetime object"""
        state = State()

        self.assertIsInstance(state.updated_at, datetime)

    def test_state_save_method(self):
        """Test State save method"""
        state = State()
        old_updated_at = state.updated_at
        state.save()

        self.assertLess(old_updated_at, state.updated_at)

    def test_state_to_dict_method(self):
        """Test State to_dict method"""
        state = State()
        state.name = "California"
        state_dict = state.to_dict()

        self.assertEqual(state_dict["__class__"], "State")
        self.assertEqual(state_dict["name"], "California")
        self.assertIsInstance(state_dict["created_at"], str)
        self.assertIsInstance(state_dict["updated_at"], str)

    def test_state_str_representation(self):
        """Test State __str__ representation"""
        state = State()
        state.name = "California"
        state_str = str(state)

        self.assertIn("[State] ({})".format(state.id), state_str)
        self.assertIn("'name': 'California'", state_str)
        self.assertIn("'created_at':", state_str)
        self.assertIn("'updated_at':", state_str)

    def test_state_save_and_reload(self):
        """Test State save and reload"""
        state = State()
        state.name = "California"
        state.save()

        loaded_state = storage.all()["State.{}".format(state.id)]
        self.assertIsInstance(loaded_state, State)
        self.assertEqual(loaded_state.name, "California")


if __name__ == "__main__":
    unittest.main()
