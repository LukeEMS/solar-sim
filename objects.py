from math import pi
class solar_object:
    def __init__(self, name, mass,radius):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.diameter = 2*radius
        self.volume = (4/3)*pi*(radius^3)
        self.density = self.mass/self.volume

    def __str__(self):
        return f"Name: {self.name} Mass: {self.mass}" 
        

    def gravitational_pull(self,other_object:'solar_object'):
        ...