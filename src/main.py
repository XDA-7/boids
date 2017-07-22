"""Program entry point"""

import typing
import boid
import window

FLOCK = typing.List[boid.Boid]
ITERATIONS = 0

window = window.Window()
flock: FLOCK = [
    boid.Boid(5, 100, 500, 500, 0),
    boid.Boid(5, 100, 550, 500, 1.5),
    boid.Boid(5, 100, 480, 500, -1.5),
    boid.Boid(5, 100, 500, 520, 3.14),
    boid.Boid(5, 100, 500, 430, 3.14)
]

for boid in flock:
    window.add_boid(boid)

while True:
    for boid in flock:
        boid.update(flock)
    window.update()
    ITERATIONS += 1
    print(ITERATIONS)
