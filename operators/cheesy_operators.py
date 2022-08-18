#!/usr/bin/env python3

# 1. Implement __ne__() for the Cheese class
# 2. Implement __mul__(), __rmul__(), and __imul__() for Cheese.
# Remember that multiplication is just repeated addition, so 
# 3 * "Edam" is "Edam/Edam/Edam".

class Cheese:

    def __init__(self, name, runniness):
        self.name = name
        self.runniness = runniness

    def __str__(self):
        return f'{self.name} (runniness: {self.runniness})'

    def __eq__(self, other):
        if isinstance(other, Cheese):
            return (self.name == other.name
                and self.runniness == other.runniness)
        return NotImplemented

    def __add__(self, other):    
        if isinstance(other, Cheese):
            newname = self.name + '/' + other.name
            newrunny = (self.runniness + other.runniness) // 2
            return Cheese(newname, newrunny)
        return NotImplemented    


# Implement __eq__() for EgalitarianCracker. These crackers
# Think they're equal to any other object of any type.
# Test this by comparing with an instance of Cheese, e.g.
# chedder == multigrain.

class EgalitarianCracker:

    def __init__(self, name):
        self.name = name

