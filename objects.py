from math import pi

class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    
class SolarSystem:
    def __init__(self):
        ...
class SolarObject:
    def __init__(self,
                 name:str,
                 mass:float,
                 radius:float,
                 orbit_rabius:float,
                 starting_position:Vector):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.diameter = 2*radius
        self.volume = (4/3)*pi*(radius^3)
        self.density = self.mass/self.volume
        self.orbit_radius = self.orbit_radius
        
    def __str__(self):
        return f"Name: {self.name} Mass: {self.mass}" 
    
    def set_position(self,x,y,z):
        self.position = Vector(x,y,z)

    def gravitational_pull(self,other_object:'SolarObject'):
        ...