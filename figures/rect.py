from decimal import Decimal
from figures.point2d import Point2d
from figures.triangle import Triangle
from figures.vector2d import make_vector_from_points


class Rect:
    a: Point2d
    b: Point2d
    c: Point2d
    d: Point2d
    tri_abc: Triangle
    is_square: bool
    center: Point2d
    diaginal_len: Decimal
    ANGLE_ERROR_TOLARANCE = 0.05

    def __str__(self) -> str:
        return f"a => {self.a}\nb => {self.b}\nc => {self.c}\nd => {self.d}"

    def is_valid_tri(self) -> bool:
        is_rect = False
        if self.is90(self.tri_abc.alpha):
            self.diaginal_len = Decimal(self.tri_abc.sidea)
            is_rect = True
            self.is_square = self.is45(self.tri_abc.beta) and self.is45(self.tri_abc.gama)
            self.calcualte_center(self.b, self.c)
            self.calculate_d(self.center, self.a)
        elif self.is90(self.tri_abc.beta):
            self.diaginal_len = Decimal(self.tri_abc.sideb)
            is_rect = True
            self.is_square = self.is45(self.tri_abc.alpha) and self.is45(self.tri_abc.gama)
            self.calcualte_center(self.a, self.c)
            self.calculate_d(self.center, self.b)
        elif self.is90(self.tri_abc.gama):
            self.diaginal_len = Decimal(self.tri_abc.sidec)
            is_rect = True
            self.is_square = self.is45(self.tri_abc.alpha) and self.is45(self.tri_abc.beta)
            self.calcualte_center(self.a, self.b)
            self.calculate_d(self.center, self.c)

        if is_rect:
            print(f"found center at {self.center}")
            print(f"found d point at {self.d}")

        return is_rect

    def is90(self, angle: Decimal) -> bool:
        return abs(90 - angle) < self.ANGLE_ERROR_TOLARANCE

    def is45(self, angle: Decimal) -> bool:
        return abs(45 - angle) < self.ANGLE_ERROR_TOLARANCE

    def calcualte_center(self, p1: Point2d, p2: Point2d) -> None:
        self.center = Point2d((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)

    def calculate_d(self, center: Point2d, p: Point2d) -> None:
        self.d = Point2d(
            (center.x - p.x) + center.x,
            (center.y - p.y) + center.y
        )

    def is_point_inside(self, x: Point2d) -> bool:
        ab = make_vector_from_points(self.a, self.b)
        am = make_vector_from_points(self.a, x)
        bc = make_vector_from_points(self.b, self.c)
        bm = make_vector_from_points(self.b, x)
        dotABAM = ab.dot(am)
        dotABAB = ab.dot(ab)
        dotBCBM = bc.dot(bm)
        dotBCBC = bc.dot(bc)

        return 0 <= dotABAM and dotABAM <= dotABAB and 0 <= dotBCBM and dotBCBM <= dotBCBC


def make_rect_with_triangle(tri: Triangle) -> Rect:
    rect = Rect()
    rect.tri_abc = tri
    rect.a = tri.a
    rect.b = tri.b
    rect.c = tri.c

    return rect
