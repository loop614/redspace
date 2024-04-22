from __future__ import annotations

from decimal import Decimal

from primary.point import Point


class Vector2d:
    x: Decimal
    y: Decimal

    def __init__(self, x: Decimal, y: Decimal) -> None:
        self.x = x
        self.y = y

    def dot(self, other: Vector2d) -> Decimal:
        return self.x * other.x + self.y * other.y


def make_vector_from_points(p1: Point, p2: Point) -> Vector2d:
    return Vector2d(p2.x - p1.x, p2.y - p1.y)
