"""Vector module"""
from math import sqrt, sin, cos

class Vector:
    """2D Vector with operations useful to the program"""
    def __init__(self, x: float, y: float):
        self.x_val = x
        self.y_val = y

    def __add__(self, other: 'Vector'):
        return Vector(self.x_val + other.x_val, self.y_val + other.y_val)

    def __sub__(self, other: 'Vector'):
        return Vector(self.x_val - other.x_val, self.y_val - other.y_val)

    def __mul__(self, other: float):
        return Vector(self.x_val * other, self.y_val * other)

    def negative(self) -> 'Vector':
        return Vector(-self.x_val, -self.y_val)

    def magnitude(self) -> float:
        return sqrt(self.x_val ** 2 + self.y_val ** 2)

    def normalized(self) -> 'Vector':
        if self.x_val == 0 and self.y_val == 0:
            return Vector(0, 0)
        magnitude = self.magnitude()
        return Vector(self.x_val / magnitude, self.y_val / magnitude)

    def rotate(self, rotation: float) -> 'Vector':
        """Rotate the vector counter-clockwise by the rotation specified in radians"""
        x_val = self.x_val * cos(rotation) - self.y_val * sin(rotation)
        y_val = self.x_val * sin(rotation) + self.y_val * cos(rotation)
        return Vector(x_val, y_val)

    def rotation(self) -> float:
        """Calculates the cosine of the angle of the vector from (0, 1)"""
        #Method: Simplification of the dot product where vector b = (0, 1) becomes
        return self.y_val / self.magnitude()

    def rotation_normalized(self) -> float:
        """Calculates the cosine as above and then normalises it from (1, -1) to (0, 1)"""
        cos_val = self.rotation()
        return (-cos_val + 1) / 2

    def str(self) -> str:
        return '(' + str(self.x_val) + ', ' + str(self.y_val) + ')'
