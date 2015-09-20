from Hoplite.people import *

a = Hero((0, 0, 0))

print(a.position)
print(a.health)

b = a.step_options()
for _ in a.step_options(3):
    print(_)



