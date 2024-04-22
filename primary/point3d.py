from decimal import Decimal

from primary.point import Point


class Point3d(Point):
    z: Decimal

    def __init__(self, x: Decimal, y: Decimal, z: Decimal) -> None:
        super().__init__(x, y)
        self.z = z

    def __str__(self) -> str:
        return f"x = {self.x}, y = {self.y}, z = {self.z}"

    def get_distance_to(self, that: 'Point3d') -> Decimal:
        return (((self.x - that.x) ** 2) + ((self.y - that.y) ** 2) + ((self.z - that.z) ** 2)).sqrt()
