from decimal import Decimal
from figure2d.base import Figure2d
from primary.point import Point
from figure2d.triangle import Triangle
from primary.point2d import Point2d
from primary.point3d import Point3d
from primary.vector2d import make_vector_from_points


class Rect(Figure2d):
    a: Point
    b: Point
    c: Point
    d: Point
    is_valid: bool
    is_square: bool
    tri_abc: Triangle
    center: Point
    diaginal_len: Decimal

    def __init__(self) -> None:
        super().__init__()

    def __str__(self) -> str:
        return f"a => {self.a}\nb => {self.b}\nc => {self.c}\nd => {self.d}"

    def calculate_is_valid(self) -> None:
        self.is_valid = False
        if self.tri_abc.alpha.is90():
            self.diaginal_len = Decimal(self.tri_abc.sidea)
            self.is_valid = True
            self.is_square = self.tri_abc.beta.is45() and self.tri_abc.gama.is45()
            self.calculate_center(self.b, self.c)
            self.calculate_d(self.center, self.a)
        elif self.tri_abc.beta.is90():
            self.diaginal_len = Decimal(self.tri_abc.sideb)
            self.is_valid = True
            self.is_square = self.tri_abc.alpha.is45() and self.tri_abc.gama.is45()
            self.calculate_center(self.a, self.c)
            self.calculate_d(self.center, self.b)
        elif self.tri_abc.gama.is90():
            self.diaginal_len = Decimal(self.tri_abc.sidec)
            self.is_valid = True
            self.is_square = self.tri_abc.alpha.is45() and self.tri_abc.beta.is45()
            self.calculate_center(self.a, self.b)
            self.calculate_d(self.center, self.c)

        if self.is_valid:
            print(f"found center at {self.center}")
            print(f"found d point at {self.d}")


    def calculate_center(self, p1: Point, p2: Point) -> None:
        if isinstance(p1, Point3d) and isinstance(p2, Point3d):
            self.center = Point3d(
                (p1.x + p2.x) / 2, (p1.y + p2.y) / 2, (p1.z + p2.z) / 2
            )
            return

        self.center = Point2d((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)

    def calculate_d(self, center: Point, p: Point) -> None:
        if isinstance(center, Point3d) and isinstance(p, Point3d):
            self.d = Point3d(
                (center.x - p.x) + center.x,
                (center.y - p.y) + center.y,
                (center.z - p.z) + center.z,
            )
            return

        self.d = Point2d((center.x - p.x) + center.x, (center.y - p.y) + center.y)

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


def make_rect_with_triangle(tri: Triangle) -> Rect:
    rect = Rect()
    rect.tri_abc = tri
    rect.a = tri.a
    rect.b = tri.b
    rect.c = tri.c
    rect.calculate_is_valid()

    return rect
