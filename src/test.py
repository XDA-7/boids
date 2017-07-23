from vector import Vector

vector = Vector(0, -1)
print(vector.rotation_normalized())
vector = Vector(0, 1)
print(vector.rotation_normalized())
vector = Vector(1, 0)
print(vector.rotation_normalized())
vector = Vector(-1, 0)
print(vector.rotation_normalized())
vector = Vector(4, 1)
print(vector.rotation_normalized())