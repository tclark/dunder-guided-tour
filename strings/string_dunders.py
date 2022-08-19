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

# Since we don't implement __str__(), the interpreter falls back to 
# printing the output of __repr__(): Parrot('Norwegian Blue', False)


# Implement __str__() and __repr__() for the Cheese class
class Cheese:

    def __init__(self, name, runniness):
        self.name = name
        self.runniness = runniness

    def __str__(self):
        return f'{self.name}, runniness: {self.runniness}'
    
    def __repr__(self):
        return f"Cheese('{self.name}', self.runniness)"


camembert = Cheese('Camembert', 6)
print(camembert)
print(repr(camembert))

