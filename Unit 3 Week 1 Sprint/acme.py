"""
Part 1
"""
import random


class Product:

    def __init__(self, name, price=10, weight=20, flammability=.5):

        self.name=name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randrange(1000000, 10000000, 1)

    def stealability(self):
        value = (self.price / self.weight)
        if value < 0.5:
            print('not so stealable...')
        if 0.5 <= value < 1:
            print('Kinda stealable.')
        else:
            print('Very stealable!')

    def explode(self):
        boom = (self.flammability * self.weight)
        if boom < 10:
            print('...fizzle')
        if 10 <= boom < 50:
            print('...booom!')
        else:
            print('...BABOOM!!')


class BoxingGlove(Product):

    def __init__(self, name, price=10, weight=10,
     flammability=.5):
        self.weight = weight
        super().__init__(self, name, price, weight, flammability)

    def explode(self):
        print("...it's a glove")

    def punch(self):
        if self.weight < 5:
            print('That tickles')
        if 5 <= self.weight < 15:
            print('OUCH!')
        else:
            print('no instructions')
