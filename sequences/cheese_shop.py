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

    def __len__(self):
        return len(self.inventory)

    def __getitem__(self, key):
        if isinstance(key, slice):
            return CheeseShop(self.proprietor, self.inventory[key]
        return self.inventory[key]

   def __setitem__(self, key, val):
       self.inventory[key] = val

   del __delitem__(self, key):
       del self.inventory[key]

   def insert(self, key, val):
       self.inventory.insert(key, val)

# One big thing to take away from this example is that we are able
# to implement our sequence easily because we are leveraging the 
# capability of the underlying list.
