from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
Cube = namedtuple("Cube", ["x", "y", "z"])
Hex = namedtuple("Hex", ["q", "r"])

directions = {'ff': Cube(0, 1, -1),
              'fr': Cube(1, 0, -1),
              'br': Cube(1, -1, 0),
              'bb': Cube(0, -1, 1),
              'bl': Cube(-1, 0, 1),
              'fl': Cube(-1, 1, 0)}


def hex_add(hex_a, hex_b):
    return Cube(hex_a.x + hex_b.x, hex_a.y + hex_b.y, hex_a.z + hex_b.z)


def hex_subtract(hex_a, hex_b):
    return Cube(hex_a.x - hex_b.x, hex_a.y - hex_b.y, hex_a.z - hex_b.z)


def hex_neighbor(start_hex, direction):
    return hex_add(start_hex, directions[direction])


def hex_distance(hex_a, hex_b):
    return max(abs(da - db) for da, db in zip(hex_a, hex_b))


def cube_add(hex_a, hex_b):
    return tuple(map(sum, zip(hex_a, hex_b)))


def range_area(start_point, distance):
    out = []
    for dx in range(-distance, distance + 1):
        for dy in range(max(-distance, -dx - distance), min(distance, -dx + distance) + 1):
            print(dx, dy)
            out += [cube_add(start_point, (dx, dy, -dx - dy))]
    return out


def cube_to_hex(cube):
    return Hex(cube.x, cube.z)


if __name__ == '__main__':
    cube1 = Cube(0, 0, 0)
    cube2 = Cube(-1, 2, -1)
    cube3 = Cube(-5, 0, 5)
    hex1 = Hex(0, 1)
    print(cube_to_hex(cube1))
    print(cube_to_hex(cube2))
    print(hex_add(cube3, cube2))
