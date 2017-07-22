"""
Boids module
The three critical rules governing boid behaviour are
1. Separation: Set velocity to move away from local boids
2. Alignment: Set velocity to move in the average direction of local boids
3. Cohesion: Set velocity to move towards the centre of mass of local boids
"""
from typing import List
from vector import Vector

TRIANGLE_POINTS = (Vector(0, 5), Vector(5, -5), Vector(-5, -5))

class Boid:
    """Simple Automaton"""
    separation_velocity_multiplier = 0.1
    alignment_velocity_multiplier = 0.1
    cohesion_velocity_multiplier = 0.1

    def __init__(self, radius: float, vision_radius: float,
                 x_position: float, y_position: float, rotation: float):
        self.radius = radius
        self.vision_radius = vision_radius
        self.vision_radius_squared = vision_radius ** 2
        self.x_position = x_position
        self.y_position = y_position
        self.rotation = rotation
        self.x_velocity = 0
        self.y_velocity = 0

    def bounding_box(self) -> tuple:
        """OBSOLETE: The boid is now represented by a triangle
        Returns the x,y coords of the top-left and bottom right corners of the bounding box"""
        upper_left_x = self.x_position - self.radius
        upper_left_y = self.y_position + self.radius
        bottom_right_x = self.x_position + self.radius
        bottom_right_y = self.y_position - self.radius
        return (upper_left_x, upper_left_y, bottom_right_x, bottom_right_y)

    def points(self) -> tuple:
        points = []
        for point in TRIANGLE_POINTS:
            rotated_point = point.rotate(self.rotation)
            points.append(rotated_point.x_val + self.x_position)
            points.append(rotated_point.y_val + self.y_position)
        return tuple(points)

    def update(self, boids: List['Boid']):
        """Adjusts the boid's velocity depending on neighbouring boids"""
        local_boids = self.find_neighbouring_boids(boids)
        print('local boids count: ' + str(local_boids.__len__()))
        separation = self.separation_velocity(local_boids) * Boid.separation_velocity_multiplier
        alignment = self.alignment_velocity(local_boids) * Boid.alignment_velocity_multiplier
        cohesion = self.cohesion_velocity(local_boids) * Boid.cohesion_velocity_multiplier
        self.x_velocity = separation.x_val + alignment.x_val + cohesion.x_val
        self.y_velocity = separation.y_val + alignment.y_val + cohesion.y_val

    def velocity(self) -> Vector:
        return Vector(self.x_velocity, self.y_velocity)

    def separation_velocity(self, local_boids: List['Boid']) -> Vector:
        """Calculates the velocity to avoid local boids"""
        locals_to_self_x = 0
        locals_to_self_y = 0
        for boid in local_boids:
            locals_to_self_x += self.x_position - boid.x_position
            locals_to_self_y += self.y_position - boid.y_position
        return Vector(locals_to_self_x, locals_to_self_y).normalized()

    def alignment_velocity(self, local_boids: List['Boid']) -> Vector:
        """Calculates the average velocity of all local boids"""
        alignment_x = 0
        alignment_y = 0
        for boid in local_boids:
            alignment_x += boid.x_velocity
            alignment_y += boid.y_velocity
        return Vector(alignment_x, alignment_y).normalized()

    def cohesion_velocity(self, local_boids: List['Boid']) -> Vector:
        """Calculates the direction towards the center of mass of all local boids"""
        position_x = 0
        position_y = 0
        boid_count = local_boids.__len__()
        for boid in local_boids:
            position_x += boid.x_position
            position_y += boid.y_position
        position_x /= boid_count
        position_y /= boid_count
        return Vector(position_x - self.x_position, position_y - self.y_position).normalized()

    def find_neighbouring_boids(self, boids: List['Boid']) -> List['Boid']:
        """Find all boids within the self's range of vision"""
        local_boids = []
        for boid in boids:
            if(boid == self):
                continue
            distance_squared = (self.x_position - boid.x_position) ** 2
            distance_squared += (self.y_position - boid.y_position) ** 2
            if distance_squared <= self.vision_radius_squared:
                local_boids.append(boid)
        return local_boids
