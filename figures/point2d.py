from decimal import Decimal


class Point2d:
    x: Decimal
    y: Decimal

    def __init__(self, x: Decimal, y: Decimal) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"x = {self.x}, y = {self.y}"

    def get_distance_to(self, that: "Point2d") -> Decimal:
        return (((self.x - that.x) ** 2) + ((self.y - that.y) ** 2)).sqrt()
