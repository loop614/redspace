import math
from figures.point2d import Point2d
from figures.vector2d import make_vector_from_points


class Rect:
    a: Point2d
    b: Point2d
    c: Point2d
    d: Point2d
    is_square: bool
    center: Point2d
    diaginal_len: float

    def __str__(self) -> str:
        return f"a => {self.a}\nb => {self.b}\nc => {self.c}\nd => {self.d}"

    def is_valid(self) -> bool:
        sidea = self.b.get_distance_to(self.c)
        sideb = self.a.get_distance_to(self.c)
        sidec = self.a.get_distance_to(self.b)

        alpha = math.degrees(
            math.acos((sideb**2 + sidec**2 - sidea**2) / (2 * sideb * sidec))
        )
        gama = math.degrees(
            math.acos((sidea**2 + sideb**2 - sidec**2) / (2 * sidea * sideb))
        )
        beta = 180 - alpha - gama
        print("found triangle with")
        print(f"angles {alpha}, {beta}, {gama}")
        print(f"sides {sidea}, {sideb}, {sidec}")

        is_rect = False
        if self.is90(alpha):
            self.diaginal_len = sidea
            is_rect = True
            self.is_square = self.is45(beta) and self.is45(gama)
            self.calcualte_center(self.b, self.c)
            self.calculate_d(self.center, self.a)
        elif self.is90(beta):
            self.diaginal_len = sideb
            is_rect = True
            self.is_square = self.is45(alpha) and self.is45(gama)
            self.calcualte_center(self.a, self.c)
            self.calculate_d(self.center, self.b)
        elif self.is90(gama):
            self.diaginal_len = sidec
            is_rect = True
            self.is_square = self.is45(alpha) and self.is45(beta)
            self.calcualte_center(self.a, self.b)
            self.calculate_d(self.center, self.c)

        if is_rect:
            print(f"found center at {self.center}")
            print(f"found d point at {self.d}")

        return is_rect

    def is90(self, angle: float) -> bool:
        return abs(90 - angle) < 0.00001

    def is45(self, angle: float) -> bool:
        return abs(45 - angle) < 0.00001

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


def make_rect_with_3_points(a: Point2d, b: Point2d, c: Point2d) -> Rect:
    rect = Rect()
    rect.a = a
    rect.b = b
    rect.c = c

    return rect
