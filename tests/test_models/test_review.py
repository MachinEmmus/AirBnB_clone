#!/usr/bin/python3

"""In this file we prove that the review file, that the class works good"""

import unittest
import pep8
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review


class Testreview(unittest.TestCase):
    """Class with the methods to prove that the review class works good"""
    def test_pep8_conformance_review(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class(self):
        """
            In this method we prove that after instantiating the class,
            its type if it corresponds to the one we want
        """
        rev1 = Review()
        self.assertEqual(rev1.__class__.__name__, "Review")

    def test_father(self):
        """
            In this method we prove that after instantiating the class,
            it really inherits from its parent class
        """
        rev1 = Review()
        self.assertTrue(issubclass(rev1.__class__, BaseModel))
