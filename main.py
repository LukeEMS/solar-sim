from objects.SolarObject import *
from objects.Vectors import *

sun = SolarObject(name="Sun",
                  mass=10**30,
                  orbit_radius=1,
                  starting_position=Vector(0,0,0),
                  starting_velocity=Vector(0,0,0))

earth = SolarObject(name="Earth",
                    mass=10*24,
                    orbit_radius=107.5,
                    starting_position=Vector(0,0,0),
                    starting_velocity=Vector(0,0,0))




print(v)