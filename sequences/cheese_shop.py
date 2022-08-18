#!/usr/bin/env python3


class Cheese:

    def __init__(self, name, runniness):
        self.name = name
        self.runniness = runniness
        self.available = False

    def __str__(self):
        return f'{self.name} (runniness: {self.runniness})'

# Now make CheeseShop a Mutable Sequence by implementing
# __getitem__(), __len__(), __setitem__(), __delitem__(),
# and insert()


class CheeseShop:
    def __init__(self, proprietor, inventory):
        self.proprietor = proprietor
        # inventory is a list of Cheeses
        self.inventory = inventory


