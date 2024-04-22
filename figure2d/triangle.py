from decimal import Decimal
import math
from figure2d.base import Figure2d
from primary.angle import Angle
from primary.point import Point


class Triangle(Figure2d):
    a: Point
    b: Point
    c: Point
    sidea: Decimal
    sideb: Decimal
    sidec: Decimal
    alpha: Angle
    beta: Angle
    gama: Angle

    def __init__(self, a: Point, b: Point, c: Point) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.calculate_sides()
        self.calculate_angles()

    def calculate_sides(self) -> None:
        self.sidea = self.b.get_distance_to(self.c)
        self.sideb = self.a.get_distance_to(self.c)
        self.sidec = self.a.get_distance_to(self.b)
        print(f"sides {self.sidea}, {self.sideb}, {self.sidec}")

    def calculate_angles(self) -> None:
        self.alpha = Angle(
            Decimal(
                math.degrees(
                    math.acos(
                        (self.sideb**2 + self.sidec**2 - self.sidea**2)
                        / (2 * self.sideb * self.sidec)
                    )
                )
            )
        )
        self.gama = Angle(
            Decimal(
                math.degrees(
                    math.acos(
                        (self.sidea**2 + self.sideb**2 - self.sidec**2)
                        / (2 * self.sidea * self.sideb)
                    )
                )
            )
        )
        self.beta = Angle(180 - self.alpha.val - self.gama.val)
        print(f"angles {self.alpha}, {self.beta}, {self.gama}")
