from figures.point2d import Point2d


class Vector2d:
    x: float
    y: float

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def dot(self, that: 'Vector2d') -> float:
        return self.x * that.x + self.y * that.y

def make_vector_from_points(p1: Point2d, p2: Point2d) -> Vector2d:
    return Vector2d(p2.x - p1.x, p2.y - p1.y)
