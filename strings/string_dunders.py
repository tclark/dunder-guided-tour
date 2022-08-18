#!/usr/bin/env python3

class Parrot:

    def __init__(self, breed, alive):
        self.breed = breed
        self.alive = alive

    def __repr__(self):
        return f"Parrot('{self.breed}', {self.alive})"


p = Parrot('Norwegian Blue', False)
#  What is printed below? Why?
print(p)


# Implement __str__() and __repr__() for the Cheese class
class Cheese:

    def __init__(self, name, runniness):
        self.name = name
        self.runniness = runniness


camembert = Cheese('Camembert', 6)
print(camembert)
print(repr(camembert))

