#!./venv/Scripts/python

""" Handles generation and display of sectors. """

from random import randrange as random
import logging


class Sector(object):

    """ A sector in space. """

    def __init__(self):
        super(Sector, self).__init__()

        self.sector_map = [['.' for x in range(8)] for x in range(10)]
        self.systems = []

    def __str__(self):
        """ Display a map of the sector. """
        output = []
        output += "Map:\n"
        for line in self.sector_map:
            for cell in line:
                output += cell + " "
            output += "\n"
        output += "System List:"
        output += self.systems
        return ''.join(output)

    def generate(self):
        """ Generate a random sector. """
        print("Generating a sector...")
        number_of_systems = random(21, 31)
        print("Will create {} systems".format(number_of_systems))

        for n in range(number_of_systems):
            print("Placing {}th/st system...".format(n))
            while True:
                x = random(0, 8)
                y = random(0, 10)
                print("{:0>2}{:0>2}".format(x, y))
                self.sector_map[y][x] = '#'
                break


if __name__ == '__main__':
    s = Sector()
    print(s)
    s.generate()
    print(s)