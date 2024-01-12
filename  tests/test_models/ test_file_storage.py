#!/usr/bin/python3

"""Unit tests for models"""

import unittest
import json
import os
import time
from unittest.mock import patch, mock_open

from models.review import Review
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    def test_base_model(self):
        # Add your test methods for BaseModel
        pass


class TestUser(unittest.TestCase):
    def test_user(self):
        # Add your test methods for User
        pass


class TestCity(unittest.TestCase):
    def test_city(self):
        # Add your test methods for City
        pass


class TestState(unittest.TestCase):
    def test_state(self):
        # Add your test methods for State
        pass


class TestAmenity(unittest.TestCase):
    def test_amenity(self):
        # Add your test methods for Amenity
        pass


class TestPlace(unittest.TestCase):
    def test_place(self):
        # Add your test methods for Place
        pass


class TestReview(unittest.TestCase):
    def test_review(self):
        # Add your test methods for Review
        pass


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = "file.json"
        self.file_storage = FileStorage()

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_file_storage_init(self):
        # Test initialization of FileStorage
        self.assertEqual(
            self.file_storage._FileStorage__file_path, "file.json")
        self.assertEqual(self.file_storage._FileStorage__objects, {})

    def test_file_storage_all(self):
        # Test the all method in FileStorage
        review = Review()
        self.file_storage.new(review)
        result = self.file_storage.all()
        key = f"{review._class.name_}.{review.id}"
        self.assertIn(key, result)
        self.assertEqual(result[key], review)

        with patch('builtins.open', new=mock_open(read_data='{"Review.": {"field": "value"}}')) as mock_file:
            self.file_storage.reload()
            mock_file.assert_called_with(self.file_path)

    def test_file_storage_new(self):
        # Test the new method in FileStorage
        obj = self.file_storage.new(Review())
        self.assertIsInstance(obj, Review)
        self.assertIn(f"{obj._class.name_}.{obj.id}",
                      self.file_storage.all())

    def test_file_storage_save(self):
        # Test the save method in FileStorage
        review = self.file_storage.new(Review())
        timestamp_before = review.updated_at
        time.sleep(0.1)  # To ensure a time difference
        self.file_storage.save()
        timestamp_after = review.updated_at
        self.assertGreater(timestamp_after, timestamp_before)

    def test_file_storage_reload(self):
        # Test the reload method in FileStorage
        review = self.file_storage.new(Review())
        self.file_storage.save()
        self.file_storage.all().clear()
        self.file_storage.reload()
        key = f"{review._class.name_}.{review.id}"
        self.assertIn(key, self.file_storage.all())
        reloaded_review = self.file_storage.all()[key]
        self.assertEqual(reloaded_review.to_dict(), review.to_dict())


if __name__ == '__main__':
    unittest.main()
