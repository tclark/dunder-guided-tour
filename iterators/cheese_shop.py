#!/usr/bin/env python3


class Cheese:

    def __init__(self, name, runniness):
        self.name = name
        self.runniness = runniness
        self.available = False

    def __str__(self):
        return f'{self.name} (runniness: {self.runniness})'

# Make CheeseShop iterable by implementng __iter__() 
# using one of our first two approaches.


class CheeseShop:
    def __init__(self, proprietor, inventory):
        self.proprietor = proprietor
        # inventory is a list of Cheeses
        self.inventory = inventory


# Now implement a custom iterator class for CheeseShops
# by implementing __next__(). Modify your CheeseShop to
# use this CheeseShopIterator

class CheeseShopIterator:
    pass

