class SolarObject:
    def __init__(self,
                 name:str,
                 mass:float,
                 radius:float,
                 orbit_radius:float,
                 starting_position:Vector,
                 starting_velocity:Vector):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.diameter = 2*radius
        self.volume = (4/3)*pi*(radius**3)
        self.density = self.mass/self.volume
        
    def __str__(self):
        return f"Name: {self.name} Mass: {self.mass}"

    def set_position(self,x,y,z):
        self.position = Vector(x,y,z)

    def gravitational_pull(self,other_object:'SolarObject'):
        ...