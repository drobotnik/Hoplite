from itertools import permutations

class Person(object):
    def __init__(self, postition):
        self.position = postition

    def step_options(self, distance=1):
        for direction in permutations((distance, -distance, 0)):
            yield(tuple(map(sum, zip(direction, self.position))))

    health = 1
    f_range = 1
    movement = 1


class Archer(Person):
    f_range = range(1, 6)


class Bomber(Person):
    f_range = range(4)


class Wizard(Person):
    f_range = range(6)


class Hero(Person):
    max_health, health = 3, 3
    max_energy, energy = 100, 100
    jump_range = range(2, 3)
    spear_range = range(3)
    max_cooldown, cooldown = 3, 0
    bash_distace = 1
    bash_range = 1


