#!/usr/bin/python3

"""In this file we prove that the place file, that the class works correctly"""

import unittest
import pep8
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review


class Teststate(unittest.TestCase):
    """Class with the methods to prove that the state class works correctly"""
    def test_pep8_conformance_state(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class(self):
        """
            In this method we prove that after instantiating the class,
            its type if it corresponds to the one we want
        """
        state1 = State()
        self.assertEqual(state1.__class__.__name__, "State")

    def test_father(self):
        """
            In this method we prove that after instantiating the class,
            it really inherits from its parent class
        """
        state1 = State()
        self.assertEqual(state1.__class__.__name__, "State")
