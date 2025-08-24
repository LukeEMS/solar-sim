import unittest
from objects.SolarSystem import SolarSystem, SolarObject
from objects.Vectors import Vector

class SolarSystemTests(unittest.TestCase):
    def test_adding_object_to_solar_system(self):

        object1 = SolarObject("test_obj",
                              10,
                              Vector(0,0,0),
                              Vector(0,0,0))
        solar_system = SolarSystem("test_solar")

        solar_system.add_object(object1)

        self.assertEqual(len(solar_system.objects),1)
        self.assertListEqual(solar_system.objects,[object1])
