from __future__ import annotations

import math
from decimal import Decimal

from primary.angle import Angle
from primary.distance import Distance


class Vector:
    x: Decimal
    y: Decimal
    z: Decimal

    def __init__(self, x: Decimal, y: Decimal, z: Decimal = Decimal(0)) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return f'x = {self.x}, y = {self.y}, z = {self.z}'

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def length(self) -> Distance:
        return Distance(Decimal(self.x**2 + self.y**2 + self.z**2).sqrt())

    def cross(self, other: Vector) -> Vector:
        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
        )

    def get_distance_to(self, other: Vector) -> Distance:
        return Distance((((self.x - other.x) ** 2) + ((self.y - other.y) ** 2) + ((self.z - other.z) ** 2)).sqrt())

    def angle_beetwen(self, other: Vector) -> Angle:
        return Angle(
            Decimal(
                math.degrees(
                    math.acos(
                        self.dot(other) /
                        (self.length().val * other.length().val),
                    ),
                ),
            ),
        )

    def dot(self, other: Vector) -> Decimal:
        return self.x * other.x + self.y * other.y + self.z * other.z
