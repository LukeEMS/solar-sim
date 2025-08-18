from objects.SolarObject import SolarObject
class SolarSystem:
    def __init__(self,
                 name:str):
        self.name = name
        self.objects = []

    def add_object(self,object:SolarObject):
        self.objects.append(object)
    
    def move_objects(self):
        # TODO: itterate over each object telling it to move 
        for object in self.objects:
            ...

