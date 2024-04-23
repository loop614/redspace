from __future__ import annotations

import math
from decimal import Decimal

from primary.angle import Angle
from primary.distance import Distance
from primary.point import Point
from redlogger import redlog


class Triangle:
    a: Point
    b: Point
    c: Point
    sidea: Distance
    sideb: Distance
    sidec: Distance
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
        redlog(f'sides {self.sidea}, {self.sideb}, {self.sidec}')

    def calculate_angles(self) -> None:
        self.alpha = Angle(
            Decimal(
                math.degrees(
                    math.acos(
                        (self.sideb.val**2 + self.sidec.val**2 - self.sidea.val**2)
                        / (2 * self.sideb.val * self.sidec.val),
                    ),
                ),
            ),
        )
        self.gama = Angle(
            Decimal(
                math.degrees(
                    math.acos(
                        (self.sidea.val**2 + self.sideb.val**2 - self.sidec.val**2)
                        / (2 * self.sidea.val * self.sideb.val),
                    ),
                ),
            ),
        )
        self.beta = Angle(180 - self.alpha.val - self.gama.val)
        redlog(f'angles {self.alpha}, {self.beta}, {self.gama}')
