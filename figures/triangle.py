from decimal import Decimal
import math
from figures.point2d import Point2d


class Triangle:
    a: Point2d
    b: Point2d
    c: Point2d
    sidea: Decimal
    sideb: Decimal
    sidec: Decimal
    alpha: Decimal
    beta: Decimal
    gama: Decimal

    def __init__(self, a: Point2d, b: Point2d, c: Point2d) -> None:
        self.a = a
        self.b = b
        self.c = c

    def calculate_sides(self) -> None:
        self.sidea = self.b.get_distance_to(self.c)
        self.sideb = self.a.get_distance_to(self.c)
        self.sidec = self.a.get_distance_to(self.b)
        print(f"sides {self.sidea}, {self.sideb}, {self.sidec}")

    def calculate_angles(self) -> None:
        self.alpha = Decimal(
            math.degrees(
                math.acos(
                    (self.sideb**2 + self.sidec**2 - self.sidea**2)
                    / (2 * self.sideb * self.sidec)
                )
            )
        )
        self.gama = Decimal(
            math.degrees(
                math.acos(
                    (self.sidea**2 + self.sideb**2 - self.sidec**2)
                    / (2 * self.sidea * self.sideb)
                )
            )
        )
        self.beta = 180 - self.alpha - self.gama
        print(f"angles {self.alpha}, {self.beta}, {self.gama}")
