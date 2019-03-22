# Class, constructor and methods
# Create a Vector object that supports addition, subtraction, dot products, and norms.
# https://www.codewars.com/kata/vector-class/train/python

import math

class Vector(object):
    def __init__(self, args):
        """ Create a vector, example: v = Vector([1,2]) """
        try:
            if not args:
                raise ValueError
            self.values = args
            self.length = len(args)
        except ValueError:
            raise ValueError("Arguments muss not be empty")
        except TypeError:
            raise ValueError("Argutments must be iterable")                 
    
    def __str__(self):
        try:
            if tuple(self.values):
                return str(tuple(self.values)).replace(" ", "")
        except:
            print("Error")
    
    def equals(self, otherVector):
        if self.values == otherVector.values:
            return True
        else:
            return False
    
    def add(self, otherVector):
        try:
            if self.length != otherVector.length:
                raise TypeError
            resultVector = list([a + b for a, b in zip(self.values, otherVector.values)])
            return Vector(resultVector)    
        except TypeError:
            raise TypeError("Vectors must have same size")

    def dot(self, otherVector):
        try:
            if self.length != otherVector.length:
                raise TypeError
            result = sum([a * b for a, b in zip(self.values, otherVector.values)])
            return result    
        except TypeError:
            raise TypeError("Vectors must have same size")        
            
    def subtract(self, otherVector):
        try:
            if self.length != otherVector.length:
                raise TypeError
            resultVector = list([a - b for a, b in zip(self.values, otherVector.values)])
            return Vector(resultVector)     
        except TypeError:
            raise TypeError("Vectors must have same size")    

    def norm(self):
        try:
            result = math.sqrt(sum([a * 2 for a in self.values]))
            return result   
        except:
            print("Unknown error") 
