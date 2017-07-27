"""Window module"""

import time
import tkinter
from typing import Tuple
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
            #TODO: the rotation is purely part of the boid's internal calculations and needs to be moved out somehow
            # possibly delta_time needs to be moved to the main loop and shared
            boid.rotation += boid.torque * delta_time
            delta = self.bounced_velocity(delta_time, boid)
            boid.x_position += delta[0]
            boid.y_position += delta[1]
            self.canvas.delete(boid.canvas_handle)
            boid.canvas_handle = self.canvas.create_polygon(boid.points())
        self.last_time = time.monotonic()
        self.window.update()

    def unconstrained_velocity(self, delta_time: float, boid: Boid) -> Tuple[float,float]:
        """Returns the x and y movements as they are"""
        delta_x = boid.x_velocity * delta_time
        delta_y = boid.y_velocity * delta_time
        return (delta_x, delta_y)
    
    def constrained_velocity(self, delta_time: float, boid: Boid) -> Tuple[float,float]:
        """Returns the x and y movements constrained as though the window edges were a wall"""
        delta_x = boid.x_velocity * delta_time
        delta_y = boid.y_velocity * delta_time
        if self.on_border(boid, delta_x, delta_y):
            return (0, 0)
        else:
            return (delta_x, delta_y)

    def bounced_velocity(self, delta_time: float, boid: Boid) -> Tuple[float,float]:
        """Returns the x and y movements, if these would take the boid outside of the window boundary
        then (0, 0) is returned and the boid is rotated 180 degrees"""
        delta_x = boid.x_velocity * delta_time
        delta_y = boid.y_velocity * delta_time
        if self.on_border(boid, delta_x, delta_y):
            boid.rotation += 3.14
            return (0, 0)
        else:
            return (delta_x, delta_y)
    
    def on_border(self, boid: Boid, delta_x: float, delta_y: float) -> bool:
        """Return true if the movement would take the boid outside of the boundary of the window"""
        return (delta_x > 0 and boid.x_position >= WIDTH or delta_x < 0 and boid.x_position < 0 or
                delta_y > 0 and boid.y_position >= HEIGHT or delta_y < 0 and boid.y_position < 0)

    def add_boid(self, boid: Boid):
        """Add a boid to the canvas"""
        boid.canvas_handle = self.canvas.create_polygon(boid.points())
        self.boids.append(boid)
