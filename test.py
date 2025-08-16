import unittest
from objects import *


class VectorTests(unittest.TestCase):
    def test_assigning_values_return_correctly(self):
        # Setup
        vector = Vector(1,2,3)
        # Assert
        self.assertEqual(1,vector.x)
        self.assertEqual(2,vector.y)
        self.assertEqual(3,vector.z)