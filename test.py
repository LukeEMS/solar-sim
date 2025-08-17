import unittest
from objects import Vector


class VectorTests(unittest.TestCase):
    def test_assigning_values_return_correctly(self):
        # Setup
        vector = Vector(1,2,3)
        # Assert
        self.assertEqual(1,vector.x)
        self.assertEqual(2,vector.y)
        self.assertEqual(3,vector.z)

    def test_equality_of_two_vectors(self):
        vector1 = Vector(1,2,3)
        vector2 = Vector(1,2,3)
        # These should return the same
        self.assertEqual(vector1,vector2)
        self.assertTrue(vector1==vector2)

    def test_subtracting_two_vectors_returns_correct_results(self):
        # Setup
        vector = Vector(4,6,8)
        other_vector = Vector(1,2,3)
        new_vector : Vector = vector - other_vector
        # Assert
        self.assertEqual(Vector(3,4,5),new_vector)
    
    def test_adding_two_vectors_returns_correct_results(self):
        # Setup
        vector = Vector(5,5,5)
        other_vector = Vector(1,2,3)
        new_vector : Vector = vector + other_vector
        # Assert
        self.assertEqual(Vector(6,7,8),new_vector)
    
    def test_multiplying_a_vector(self):
        # Setup
        vector = Vector(1,2,3)
        multiplier = float(2)
        new_vector : Vector = vector * multiplier
        # Assert
        self.assertEqual(Vector(2,4,6),new_vector)

    def test_dividing_a_vector(self):
        # Setup
        vector = Vector(6,9,12)
        divider = float(3)
        new_vector : Vector = vector/divider
        # Assert
        self.assertEqual(Vector(2,3,4),new_vector)

    def test_sum_of_vector(self):
        vector = Vector(1,2,3)
        result = vector.sum()
        self.assertEqual(6,result)
    
    def test_magnitude_of_vector(self):
        vector = Vector(1,2,3)
        square = vector**2
        total_of_square = square.sum()
        mag = total_of_square**(0.5)
        self.assertEqual(mag, vector.magnitude())

if __name__ == "__main_":
    unittest.main()

    