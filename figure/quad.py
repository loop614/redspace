from __future__ import annotations

from decimal import Decimal

from figure.triangle import Triangle
from primary.distance import Distance
from primary.vector import Vector
from redlogger import redlog


class Quad:
    a: Vector
    b: Vector
    c: Vector
    d: Vector
    tri_abc: Triangle
    center: Vector
    is_rect: bool
    is_square: bool
    is_tilted: bool
    sideab: Distance
    sidebc: Distance
    sidecd: Distance
    sideda: Distance
    diaginal_len: Distance

    def __str__(self) -> str:
        return f'a => {self.a}\nb => {self.b}\nc => {self.c}\nd => {self.d}'

    def get_points(self) -> list[Vector]:
        return [self.a, self.b, self.c, self.d]

    def calculate_is_rect(self) -> None:
        self.is_rect = False
        if self.tri_abc.alpha.is90():
            self.diaginal_len = self.tri_abc.sidea
            self.is_rect = True
            self.is_square = self.tri_abc.beta.is45() and self.tri_abc.gamma.is45()
            self.calculate_d(self.b, self.c, self.a)
        elif self.tri_abc.beta.is90():
            self.diaginal_len = self.tri_abc.sideb
            self.is_rect = True
            self.is_square = self.tri_abc.alpha.is45() and self.tri_abc.gamma.is45()
            self.calculate_d(self.a, self.c, self.b)
        elif self.tri_abc.gamma.is90():
            self.diaginal_len = self.tri_abc.sidec
            self.is_rect = True
            self.is_square = self.tri_abc.alpha.is45() and self.tri_abc.beta.is45()
            self.calculate_d(self.a, self.b, self.c)

        if self.is_rect:
            self.calculate_is_tilted()
            self.calculate_sides()
            redlog(f'found center at {self.center}')
            redlog(f'found d point at {self.d}')
            if self.is_tilted:
                redlog('it is tilted')
            else:
                redlog('it is not tilted')

    def calculate_d(
        self,
        centerLeft: Vector,
        centerRight: Vector,
        dOpposite: Vector,
    ) -> None:
        self.calculate_center(centerLeft, centerRight)
        self.d = Vector(
            (self.center.x - dOpposite.x) + self.center.x,
            (self.center.y - dOpposite.y) + self.center.y,
            (self.center.z - dOpposite.z) + self.center.z,
        )

    def calculate_center(self, p1: Vector, p2: Vector) -> None:
        self.center = Vector(
            (p1.x + p2.x) / 2,
            (p1.y + p2.y) / 2,
            (p1.z + p2.z) / 2,
        )

    def calculate_sides(self) -> None:
        self.sideab = self.a.get_distance_to(self.b)
        self.sidebc = self.b.get_distance_to(self.c)
        self.sidecd = self.c.get_distance_to(self.d)
        self.sideda = self.d.get_distance_to(self.a)

    def calculate_is_tilted(self) -> None:
        self.is_tilted = not (
            Vector(Decimal(1), Decimal(0)).angle_beetwen(self.b - self.a).is0()
            or Vector(Decimal(1), Decimal(0)).angle_beetwen(self.c - self.b).is0()
            or Vector(Decimal(1), Decimal(0)).angle_beetwen(self.d - self.c).is0()
            or Vector(Decimal(1), Decimal(0)).angle_beetwen(self.d - self.a).is0()
        )

    def is_point_inside(self, x: Vector) -> bool:
        """
        https://stackoverflow.com/questions/2752725/finding-whether-a-point-lies-inside-a-rectangle-or-not
        """
        if not self.is_rect:
            redlog('ERROR: is_point_inside not rect quad not implemented')
            return False

        ab = self.b - self.a
        am = x - self.a
        bc = self.c - self.b
        bm = x - self.b
        dotABAM = ab.dot(am)
        dotABAB = ab.dot(ab)
        dotBCBM = bc.dot(bm)
        dotBCBC = bc.dot(bc)

        return (
            0 <= dotABAM and dotABAM <= dotABAB and 0 <= dotBCBM and dotBCBM <= dotBCBC
        )


def make_quad_with_triangle(tri: Triangle) -> Quad:
    quad = Quad()
    quad.tri_abc = tri
    quad.a = tri.a
    quad.b = tri.b
    quad.c = tri.c
    quad.calculate_is_rect()

    return quad
