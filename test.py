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

    def test_subtracting_two_vectors_returns_correct_results(self):
        # Setup
        vector = Vector(1,2,3)
        other_vector = Vector(4,5,6)
        new_vector = vector + other_vector
        # Assert
        self.assertEqual(5,new_vector.x)
        self.assertEqual(7,new_vector.y)
        self.assertEqual(9,new_vector.z)
    
    def test_adding_two_vectors_returns_correct_results(self):
        # Setup
        vector = Vector(5,5,5)
        other_vector = Vector(1,2,3)
        new_vector = vector - other_vector
        # Assert
        self.assertEqual(4,new_vector.x)
        self.assertEqual(3,new_vector.y)
        self.assertEqual(2,new_vector.z)
    


if __name__ == "__main_":
    unittest.main()