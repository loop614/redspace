from decimal import Decimal

from primary.point import Point


class Point2d(Point):
    def __init__(self, x: Decimal, y: Decimal) -> None:
        super().__init__(x, y)
