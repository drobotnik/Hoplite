def hex_distance(a, b):
    return max(abs(da - db) for da, db in zip(a, b))


def cube_add(a, b):
    return tuple(map(sum, zip(a, b)))


def range_area(start_point, distance):
    out = []
    for dx in range(-distance, distance + 1):
        for dy in range(max(-distance, -dx - distance), min(distance, -dx + distance) + 1):
            print(dx, dy)
            out += [cube_add(start_point, (dx, dy, -dx - dy))]
    return out


if __name__ == '__main__':
    x = (0, 0, 0)
    y = (-2, 4, -2)

    print(hex_distance(x, y))
    range_area(x, 4)
