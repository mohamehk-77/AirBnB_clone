#!/usr/bin/python3
"""
Unit tests for Review class
"""
import unittest
from datetime import datetime
from models.review import Review
from models import storage
import os


class TestReview(unittest.TestCase):
    """Test cases for Review class"""

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

    def test_review_instance_creation(self):
        """Test Review instance creation"""
        review = Review()

        self.assertIsInstance(review, Review)
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(review, "text"))

    def test_review_attributes(self):
        """Test Review attributes"""
        review = Review()
        review.place_id = "123"
        review.user_id = "456"
        review.text = "A great place to stay!"

        self.assertEqual(review.place_id, "123")
        self.assertEqual(review.user_id, "456")
        self.assertEqual(review.text, "A great place to stay!")

    def test_review_id_generation(self):
        """Test Review id generation"""
        review1 = Review()
        review2 = Review()

        self.assertNotEqual(review1.id, review2.id)

    def test_review_created_at_datetime(self):
        """Test Review created_at is a datetime object"""
        review = Review()

        self.assertIsInstance(review.created_at, datetime)

    def test_review_updated_at_datetime(self):
        """Test Review updated_at is a datetime object"""
        review = Review()

        self.assertIsInstance(review.updated_at, datetime)

    def test_review_save_method(self):
        """Test Review save method"""
        review = Review()
        old_updated_at = review.updated_at
        review.save()

        self.assertLess(old_updated_at, review.updated_at)

    def test_review_to_dict_method(self):
        """Test Review to_dict method"""
        review = Review()
        review.place_id = "123"
        review.user_id = "456"
        review.text = "A great place to stay!"
        review_dict = review.to_dict()

        self.assertEqual(review_dict["__class__"], "Review")
        self.assertEqual(review_dict["place_id"], "123")
        self.assertEqual(review_dict["user_id"], "456")
        self.assertEqual(review_dict["text"], "A great place to stay!")
        self.assertIsInstance(review_dict["created_at"], str)
        self.assertIsInstance(review_dict["updated_at"], str)

    def test_review_str_representation(self):
        """Test Review __str__ representation"""
        review = Review()
        review.place_id = "123"
        review.user_id = "456"
        review.text = "A great place to stay!"
        review_str = str(review)

        self.assertIn("[Review] ({})".format(review.id), review_str)
        self.assertIn("'place_id': '123'", review_str)
        self.assertIn("'user_id': '456'", review_str)
        self.assertIn("'text': 'A great place to stay!'", review_str)
        self.assertIn("'created_at':", review_str)
        self.assertIn("'updated_at':", review_str)

    def test_review_save_and_reload(self):
        """Test Review save and reload"""
        review = Review()
        review.place_id = "123"
        review.user_id = "456"
        review.text = "A great place to stay!"
        review.save()

        loaded_review = storage.all()["Review.{}".format(review.id)]
        self.assertIsInstance(loaded_review, Review)
        self.assertEqual(loaded_review.place_id, "123")
        self.assertEqual(loaded_review.user_id, "456")
        self.assertEqual(loaded_review.text, "A great place to stay!")


if __name__ == "__main__":
    unittest.main()
