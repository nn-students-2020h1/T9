import math


class Squares:
    def __init__(self):
        pass

    def square_round(self, radius):
        if type(radius) not in [int, float]:
            raise TypeError("Wrong Type")
        if (radius<0):
            raise ValueError("Negative Radius")
        return radius**2*math.pi

    def square_rectangle(self, widht, height):
        if type(widht) and type(height) not in [int, float]:
            raise TypeError("Wrong Type")
        if widht<0 or height<0:
            raise ValueError("Negative Values")
        return widht*height

    def square_triangle(self, a, h):
        if type(a) and type(h) not in [int, float]:
            raise TypeError("Wrong Type")
        if a < 0 or h < 0:
            raise ValueError("Negative Values")
        return a*h/2


        
