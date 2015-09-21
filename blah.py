from collections import namedtuple

Hex = namedtuple('Hexs', ['x', 'y', 'z'])

h = Hex(11, 12, 13)

print(h.x)