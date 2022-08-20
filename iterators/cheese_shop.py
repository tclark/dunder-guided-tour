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

    def __iter__(self):
        for cheese in self.inventory:
            # It makes me happy to write a line like the one below.
            yield cheese

# Now implement a custom iterator class for CheeseShops
# by implementing __next__(). Modify your CheeseShop to
# use this CheeseShopIterator

class CheeseShop2:
    def __init__(self, proprietor, inventory):
        self.proprietor = proprietor
        # inventory is a list of Cheeses
        self.inventory = inventory

    def __iter__(self):
        return CheeseShopIterator(self)

class CheeseShopIterator:
    def __init__(self, shop):
        self.inventory = shop.inventory
        self.index = 0

    def __next__(self):
        if self.index >= len(self.shop):
            raise StopIteration()
        item = self.inventory[self.index]
        self.index += 1
        return item

    def __iter__(self):
        # An iterator should return itself
        return self

if __name__ == '__main__':
    cheeses = [
          Cheese('Brie', 4)
        , Cheese('Edam', 1)
        , Cheese('Parmesan', 0)
    ]

shop1 = CheeseShop('Wensleydale', cheeses)
print('Generator-based iterator')
for cheese in shop1:
    print(cheese)
    
shop2 = CheeseShop('Wensleydale', cheeses)
print('Custom iterator')
for cheese in shop2:
    print(cheese)
