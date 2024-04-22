from __future__ import annotations

from figure.triangle import Triangle
from primary.distance import Distance
from primary.point import Point
from primary.vector import make_vector_from_points


class Quad:
    a: Point
    b: Point
    c: Point
    d: Point
    sideab: Distance
    sidebc: Distance
    sidecd: Distance
    sideda: Distance
    is_rect: bool
    is_square: bool
    tri_abc: Triangle
    center: Point
    diaginal_len: Distance

    def __init__(self) -> None:
        super().__init__()

    def __str__(self) -> str:
        return f'a => {self.a}\nb => {self.b}\nc => {self.c}\nd => {self.d}'

    def calculate_is_rect(self) -> None:
        self.is_rect = False
        if self.tri_abc.alpha.is90():
            self.diaginal_len = self.tri_abc.sidea
            self.is_rect = True
            self.is_square = self.tri_abc.beta.is45() and self.tri_abc.gama.is45()
            self.calculate_d(self.b, self.c, self.a)
        elif self.tri_abc.beta.is90():
            self.diaginal_len = self.tri_abc.sideb
            self.is_rect = True
            self.is_square = self.tri_abc.alpha.is45() and self.tri_abc.gama.is45()
            self.calculate_d(self.a, self.c, self.b)
        elif self.tri_abc.gama.is90():
            self.diaginal_len = self.tri_abc.sidec
            self.is_rect = True
            self.is_square = self.tri_abc.alpha.is45() and self.tri_abc.beta.is45()
            self.calculate_d(self.a, self.b, self.c)

        if self.is_rect:
            self.calculate_sides()
            print(f'found center at {self.center}')
            print(f'found d point at {self.d}')

    def calculate_d(self, centerLeft: Point, centerRight: Point, dOpposite: Point) -> None:
        self.calculate_center(centerLeft, centerRight)
        self.d = Point(
            (self.center.x - dOpposite.x) + self.center.x,
            (self.center.y - dOpposite.y) + self.center.y,
            (self.center.z - dOpposite.z) + self.center.z,
        )

    def calculate_center(self, p1: Point, p2: Point) -> None:
        self.center = Point(
            (p1.x + p2.x) / 2, (p1.y + p2.y) / 2, (p1.z + p2.z) / 2,
        )

    def calculate_sides(self) -> None:
        self.sideab = self.a.get_distance_to(self.b)
        self.sidebc = self.b.get_distance_to(self.c)
        self.sidecd = self.c.get_distance_to(self.d)
        self.sideda = self.d.get_distance_to(self.a)

    def is_point_inside(self, x: Point) -> bool:
        ab = make_vector_from_points(self.a, self.b)
        am = make_vector_from_points(self.a, x)
        bc = make_vector_from_points(self.b, self.c)
        bm = make_vector_from_points(self.b, x)
        dotABAM = ab.dot(am)
        dotABAB = ab.dot(ab)
        dotBCBM = bc.dot(bm)
        dotBCBC = bc.dot(bc)

        return (
            0 <= dotABAM and dotABAM <= dotABAB and 0 <= dotBCBM and dotBCBM <= dotBCBC
        )


def make_quad_with_triangle(tri: Triangle) -> Quad:
    rect = Quad()
    rect.tri_abc = tri
    rect.a = tri.a
    rect.b = tri.b
    rect.c = tri.c
    rect.calculate_is_rect()

    return rect
