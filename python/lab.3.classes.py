import numpy as np

class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
        
    def volume(self):
        return np.pi * np.power(self.radius, 2) * self.height

radius = int(input('Введіть радіус циліндру : '))
height = int(input('Введіть висоту циліндру : '))

cylinder = Cylinder(radius, height)  
print("Об'єм циліндра:", cylinder.volume())