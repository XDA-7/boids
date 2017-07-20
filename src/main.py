import boid

window = boid.Window()
flock = [
boid.Boid(5, 30, 500, 500, 0, 0),
boid.Boid(5, 30, 520, 500, 0, 0),
boid.Boid(5, 30, 480, 500, 0, 0),
boid.Boid(5, 30, 500, 520, 0, 0),
boid.Boid(5, 30, 500, 480, 0, 0)
]

for boid in flock:
    window.add_boid(boid)

for boid in flock:
    boid.update(flock)

while True:
    # for boid in flock:
    #     boid.update(flock)
    window.update()
