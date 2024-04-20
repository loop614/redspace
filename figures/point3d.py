import math


class Point3d:
    x: float
    y: float
    z: float

    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return f"x = {self.x}, y = {self.y}, z = {self.z}"

    def get_distance_to(self, that: 'Point3d') -> float:
        return math.sqrt(math.pow(self.x - that.x, 2) + math.pow(self.y - that.y, 2) + math.pow(self.z - that.z, 2))
