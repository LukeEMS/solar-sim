class Vector:
    def __init__(self,
                 x:float,
                 y:float,
                 z:float):
        self.x = x
        self.y = y
        self.z = z
        self.sum = self.__sum()
        self.magnitude = self.__magnitude()

    def __str__(self):
        return f"({self.x},\n{self.y},\n{self.z})"
    
    def __sub__(self,other_vector:'Vector')->'Vector':
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
    
    def __add__(self,other_vector:'Vector')->'Vector':
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

    def __pow__(self,exponent:float)->'Vector':
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

    def __mul__(self,multiplier:float)->'Vector':
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

    def __truediv__(self,divider:float)->'Vector':
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
    
    def __eq__(self,other_vector:'Vector')->bool:
        if ((self.x == other_vector.x) & (self.y == other_vector.y) & (self.z == other_vector.z)):
            return True
        else:
            return False

    def __sum(self)->float:
        return self.x+self.y+self.z

    def __magnitude(self)->float:
        total = (self.x**2) + (self.y**2) + (self.z**2)
        return total**(0.5)