"""Program entry point"""

import random
import typing
from boid import Boid
import window

FLOCK = typing.List[Boid]
ITERATIONS = 0

def random_flock(size: int) -> FLOCK:
    flock: FLOCK = []
    rng = random.Random()
    for i in range(size):
        x_pos = rng.randrange(100, 900)
        y_pos = rng.randrange(100, 900)
        rot = (rng.random() -0.5) * 3.14
        flock.append(Boid(5, 100, x_pos, y_pos, rot))
    return flock

window = window.Window()
# flock: FLOCK = [
#     Boid(5, 100, 500, 500, 3.14),
#     #Boid(5, 100, 550, 500, 0)
#     #Boid(5, 100, 550, 500, 1.5),
#     #Boid(5, 100, 480, 500, -1.5),
#     #Boid(5, 100, 500, 520, 3.14),
#     #Boid(5, 100, 500, 430, 3.14)
# ]

#flock[0].torque = 1.5

flock = random_flock(100)

for boid in flock:
    window.add_boid(boid)

while True:
    for boid in flock:
        boid.update(flock)
    window.update()
    ITERATIONS += 1
    print(ITERATIONS)
