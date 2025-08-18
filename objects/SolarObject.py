from objects.Vectors import Vector
from objects.Constants import GRAVITATIONAL_CONSTANT as g
from math import pi

class SolarObject:
    def __init__(self,
                 name:str,
                 mass:float,
                 orbit_radius:float,
                 starting_position:Vector,
                 starting_velocity:Vector):
        self.name = name
        self.mass = mass
        self.orbit_radius = orbit_radius
        self.position = starting_position
        self.velocity = starting_velocity
        self.accleration = Vector(0,0,0)
        
    def __str__(self):
        return f"Name: {self.name} Mass: {self.mass}"

    def set_position(self,x:float,y:float,z:float):
        self.position = Vector(x,y,z)
    
    def gravitational_pull(self,other_object:'SolarObject')->Vector:
        diff_vector : Vector = self - other_object
        acceleration : Vector = g * (other_object.mass)/(diff_vector.magnitude)
        return acceleration

    def move(self,steps:int):
        for i in range(1,steps):
            self.position = self.position + self.velocity
            self.velocity = self.velocity + self.accleration