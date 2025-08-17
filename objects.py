from math import pi

class Vector:
    def __init__(self,
                 x:float,
                 y:float,
                 z:float):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x},\n{self.y},\n{self.z})"
    
    def __sub__(self,other_vector:'Vector'):
        """
        Overload for subtracting two Vectors. 
        Subtracts each component of the two Vectors
        """
        output_vector = Vector(
            self.x - other_vector.x,
            self.y - other_vector.y,
            self.z - other_vector.z
        )
        return output_vector
    
    def __add__(self,other_vector:'Vector'):
        """
        Overload for adding two Vectors. 
        Adds each component of the two Vectors
        """
        output_vector = Vector( 
            self.x + other_vector.x,
            self.y + other_vector.y,
            self.z + other_vector.z
        )
        return output_vector

    def __pow__(self,exponent:float):
        """
        Overload for raising a Vector to the power. 
        Raise each element to the power of the exponent
        """
        output_vector = Vector(
            self.x**exponent,
            self.y**exponent,
            self.z**exponent
            )
        return output_vector

    def __mul__(self,multiplier:float):
        """
        Overload for multiplying the Vector.
        Multiplys each element by the multiplier
        """
        output_vector = Vector(
            self.x*multiplier,
            self.y*multiplier,
            self.z*multiplier
            )
        return output_vector

    def __truediv__(self,divider:float):
        """
        Overload for dividing the Vector.
        Multiplys each element by the divider
        """
        output_vector = Vector(
            self.x/divider,
            self.y/divider,
            self.z/divider
            )
        return output_vector
    
    def __eq__(self,other_vector:'Vector'):
        if (self.x==other_vector.x) & (self.y == other_vector.y) & (self.z == other_vector.z):
            return True
        else:
            return False

    
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