"""
Boids module
The three critical rules governing boid behaviour are
1. Separation: Steer away from individual boids
2. Alignment: Steer in a similar direction of local boids
3. Cohesion: Steer toward the center of mass of local boids
"""
from typing import List
from vector import Vector

TRIANGLE_POINTS = (Vector(0, -5), Vector(5, 5), Vector(-5, 5))
VISION_ANGLE = -0.6
SPEED = 50

class Boid:
    """Simple Automaton"""
    def __init__(self, radius: float, vision_radius: float,
                 x_position: float, y_position: float, rotation: float):
        self.radius = radius
        self.vision_radius = vision_radius
        self.vision_radius_squared = vision_radius ** 2
        self.x_position = x_position
        self.y_position = y_position
        self.rotation = rotation
        self.torque = 0
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
        direction = Vector(0, -1).rotate(self.rotation)
        self.x_velocity = direction.x_val * SPEED
        self.y_velocity = direction.y_val * SPEED
        if local_boids.__len__() == 0:
            self.torque = 0
            return
        separation = self.separation_velocity(local_boids).rotate(-self.rotation)
        print('separation velocity: ' + separation.str())
        if separation.x_val < 0:
            self.torque = -separation.rotation_normalized()
        else:
            self.torque = separation.rotation_normalized()
        print('torque: ' + str(self.torque))

        # alignment = self.alignment_velocity(local_boids) * Boid.alignment_velocity_multiplier
        # cohesion = self.cohesion_velocity(local_boids) * Boid.cohesion_velocity_multiplier

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
            if boid == self:
                continue
            if (self.in_range(boid.x_position, boid.y_position) and
                    not self.in_blind_spot(boid.x_position, boid.y_position)):
                local_boids.append(boid)
        return local_boids

    def in_range(self, x_val: float, y_val: float) -> bool:
        """Return true if the position is within the vision range"""
        distance_squared = (self.x_position - x_val) ** 2
        distance_squared += (self.y_position - y_val) ** 2
        return distance_squared <= self.vision_radius_squared

    def in_blind_spot(self, x_val: float, y_val: float) -> bool:
        """Return true if the position is in the boids blind spot"""
        self_to_boid = Vector(x_val - self.x_position, y_val - self.y_position).rotate(self.rotation)
        rotation = self_to_boid.rotation()
        return rotation < VISION_ANGLE
