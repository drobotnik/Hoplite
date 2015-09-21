from Hoplite.hex_maths import *


class Map(object):
    Nq = 3
    Nr = 2

    def __init__(self):
        self.map_array = []
        for x in range((self.Nq * 2) + 1):
            row = []
            for y in range((self.Nr * 2) + 1):
                if abs(x - self.Nq + y - self.Nr) < self.Nr + 1:
                    row += ['y']
                else:
                    row += ['n']
            self.map_array += [row]


    def lookup_cube(self, cube_a):
        return cube_a.x + self.Nq, cube_a.y + self.Nr + min(0, self.Nr)


a = Map()

for _ in a.map_array:
    print(_)