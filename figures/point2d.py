import math


class Point2d:
    x: float
    y: float

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"x = {self.x}, y = {self.y}"

    def get_distance_to(self, that: 'Point2d') -> float:
        return math.sqrt(math.pow(self.x - that.x, 2) + math.pow(self.y - that.y, 2))
