"""Window module"""

import time
import tkinter
from boid import Boid

HEIGHT = 1000
WIDTH = 1000

class Window:
    """The main window in which the process will be hosted"""
    def __init__(self):
        self.window = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.window, height=HEIGHT, width=WIDTH)
        self.canvas.pack()
        self.last_time = time.monotonic()
        self.boids = []

    def update(self):
        """Event loop body"""
        delta_time = time.monotonic() - self.last_time
        for boid in self.boids:
            boid.rotation += boid.torque * delta_time
            delta_x = boid.x_velocity * delta_time
            if delta_x > 0 and boid.x_position >= WIDTH or delta_x < 0 and boid.x_position < 0:
                delta_x = 0
            delta_y = boid.y_velocity * delta_time
            if delta_y > 0 and boid.y_position >= HEIGHT or delta_y < 0 and boid.y_position < 0:
                delta_y = 0
            boid.x_position += delta_x
            boid.y_position += delta_y
            #self.canvas.move(boid.canvas_handle, delta_x, delta_y)
            self.canvas.delete(boid.canvas_handle)
            boid.canvas_handle = self.canvas.create_polygon(boid.points())
        self.last_time = time.monotonic()
        self.window.update()

    def add_boid(self, boid: Boid):
        """Add a boid to the canvas"""
        boid.canvas_handle = self.canvas.create_polygon(boid.points())
        self.boids.append(boid)
