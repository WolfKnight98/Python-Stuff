## Simple python circle area calculator

# Import modules
import math

# Main class 
class Circle(object):
    """ A simple circle area calculator """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2.0

""" Example Use:
    
    c = Cirlce(10) 

    c.radius

    c.area()
"""