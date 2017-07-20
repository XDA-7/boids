"""
Boids module
The three critical rules governing boid behaviour are
1. Separation: Set velocity to move away from local boids
2. Alignment: Set velocity to move in the average direction of local boids
3. Cohesion: Set velocity to move towards the centre of mass of local boids
"""
import time
import tkinter

class Window:
    """The main window in which the process will be hosted"""
    def __init__(self):
        self.window = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.window, bg='grey', height=1000, width=1000)
        self.canvas.pack()
        self.last_time = time.monotonic()
        self.boids = []

    def update(self):
        """Event loop body"""
        delta_time = time.monotonic() - self.last_time
        for boid in self.boids:
            delta_x = boid.x_velocity * delta_time
            delta_y = boid.y_velocity * delta_time
            self.canvas.move(boid.canvas_handle, delta_x, delta_y)
        self.last_time = time.monotonic()
        self.window.update()

    def add_boid(self, boid):
        """Add a boid to the canvas"""
        boid.canvas_handle = self.canvas.create_oval(boid.bounding_box(), fill='blue')
        self.boids.append(boid)

class Boid:
    """Simple Automaton"""
    def __init__(self, radius, vision_radius, x_position, y_position, x_velocity, y_velocity):
        self.radius = radius
        self.vision_radius = vision_radius
        self.vision_radius_squared = vision_radius ** 2
        self.x_position = x_position
        self.y_position = y_position
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity

    def bounding_box(self):
        """Returns the x,y coords of the top-left and bottom right corners of the bounding box"""
        upper_left_x = self.x_position - self.radius
        upper_left_y = self.y_position + self.radius
        bottom_right_x = self.x_position + self.radius
        bottom_right_y = self.y_position - self.radius
        return (upper_left_x, upper_left_y, bottom_right_x, bottom_right_y)

    def update(self, boids):
        """Adjusts the boid's velocity depending on neighbouring boids"""
        local_boids = self.find_neighbouring_boids(boids)
        print(local_boids)

    def separation_velocity(self, local_boids):
        """Calculates the velocity to avoid local boids"""
        pass


    def find_neighbouring_boids(self, boids):
        """Find all boids within the self's range of vision"""
        local_boids = []
        for boid in boids:
            distance_squared = (self.x_position - boid.x_position) ** 2
            distance_squared += (self.y_position - boid.y_position) ** 2
            if distance_squared <= self.vision_radius_squared:
                local_boids.append(boid)
        return local_boids
