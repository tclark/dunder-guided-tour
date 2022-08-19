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

    def __ne__(self, other):
        if isinstance(other, Cheese):
            return not self.__eq__(self, other)
        return NotImplemented

    def __add__(self, other):    
        if isinstance(other, Cheese):
            newname = self.name + '/' + other.name
            newrunny = (self.runniness + other.runniness) // 2
            return Cheese(newname, newrunny)
        return NotImplemented    

    def __mul__(self, other):    
        if isinstance(other, int):
            if other < 0:
                raise ValueError('Can only multiply Cheese by a positive int')
            newname = (self.name + '/') * other
            return Cheese(newname[:-1], self.runniness)
        return NotImplemented

    def __rmul__(self, other):    
        if isinstance(other, int):
            return self.__mul__(other)
        return NotImplemented

    def __imul__(self, other):    
        if isinstance(other, int):
            return self.__mul__(other)
        return NotImplemented


edam = Cheese('edam', 1)
triple_edam = edam * 3
print(triple_edam)
quad_edam = 4 * edam
print(quad_edam)
edam *= 2
print(edam)
# We can't multiply a Cheese with a non-positive number 
# because there's no sensible interpretation of that
#edam * -1 # raises an exception

# Implement __eq__() for EgalitarianCracker. These crackers
# Think they're equal to any other object of any type.
# Test this by comparing with an instance of Cheese, e.g.
# chedder == multigrain.

class EgalitarianCracker:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return True

cheddar = Cheese('cheddar', 1)
multigrain = EgalitarianCracker('multigrain')
print(cheddar == multigrain)

