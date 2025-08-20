from typing import List
from objects.Vectors import Vector
from objects.Constants import GRAVITATIONAL_CONSTANT as g
from math import pi
class SolarSystem:
    def __init__(self,
                 name:str):
        self.name = name
        self.objects: List[SolarObject] = []

    def add_object(self,object:SolarObject):
        self.objects.append(object)
    
    def move_objects(self,steps:int):
        # TODO: itterate over each object telling it to move 
        for i in range(0,steps):
            for object in self.objects:
                object.move(solar_system=self)

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

    def set_position(self,
                     x:float,
                     y:float,
                     z:float):
        self.position = Vector(x,y,z)
    
    def acceleration_calc(self,solar_system:SolarSystem)->Vector:
        for planet in solar_system.objects:
            diff_vector : Vector = self.position - planet.position
            acceleration : Vector = (g * (planet.mass)/(diff_vector.magnitude))
            self.acceleration = acceleration

    def move(self,
             solar_system:SolarSystem):
        self.position = self.position + self.velocity
        self.velocity = self.velocity + self.accleration
        self.acceleration_calc(solar_system=solar_system)