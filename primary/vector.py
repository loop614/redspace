from __future__ import annotations

import math
from decimal import Decimal

from primary.angle import Angle
from primary.point import Point


class Vector:
    x: Decimal
    y: Decimal
    z: Decimal
    p1: Point
    p2: Point

    def __init__(self, x: Decimal, y: Decimal, z: Decimal = Decimal(0)) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __len__(self):
        return (self.x**2 + self.y**2 + self.z**2).sqrt()

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def cross(self, other: Vector) -> Vector:
        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
        )

    def dot(self, other: Vector) -> Decimal:
        return self.x * other.x + self.y * other.y + self.z * other.z

    def angle_beetwen(self, other: Vector) -> Angle:
        return Angle(
            Decimal(
                math.degrees(
                    math.acos(self.dot(other) / (len(self) * len(other))),
                ),
            ),
        )


def make_vector_from_points(p1: Point, p2: Point) -> Vector:
    v = Vector(p2.x - p1.x, p2.y - p1.y)
    v.p1 = p1
    v.p2 = p2

    return v
