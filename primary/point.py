from __future__ import annotations

from decimal import Decimal

from primary.distance import Distance


class Point():
    x: Decimal
    y: Decimal
    z: Decimal

    def __init__(self, x: Decimal, y: Decimal, z: Decimal = Decimal(0)) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return f'x = {self.x}, y = {self.y}, z = {self.z}'

    def get_distance_to(self, other: Point) -> Distance:
        return Distance((((self.x - other.x) ** 2) + ((self.y - other.y) ** 2) + ((self.z - other.z) ** 2)).sqrt())
