from figure3d.base import Figure3d
from primary.point3d import Point3d
from figure2d.rect import Rect, make_rect_with_triangle
from figure2d.triangle import Triangle


class Cuboid(Figure3d):
    a: Point3d
    b: Point3d
    c: Point3d
    d: Point3d
    rect1: Rect
    is_rectangular_prism: bool
    is_cube: bool
    second_rect_point: Point3d
    DISTANCE_ERROR_TOLARANCE = 0.05

    def __init__(self, a: Point3d, b: Point3d, c: Point3d, d: Point3d) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.calculate_is_rectangular_prism()
        self.calculate_is_cube()

    def calculate_is_rectangular_prism(self) -> None:
        self.is_rectangular_prism = False
        points_for_cuboid = [self.a, self.b, self.c, self.d]
        for point in points_for_cuboid:
            candidate_for_rect = []
            for point2 in points_for_cuboid:
                if point is not point2:
                    candidate_for_rect.append(point2)

            xpivot = candidate_for_rect[0].x
            ypivot = candidate_for_rect[0].y
            zpivot = candidate_for_rect[0].z
            x_same = y_same = z_same = True

            for candidate in candidate_for_rect[1:]:
                if xpivot != candidate.x:
                    x_same = False
                if ypivot != candidate.y:
                    y_same = False
                if zpivot != candidate.z:
                    z_same = False

            if not x_same and not y_same and not z_same:
                continue

            tri = Triangle(
                candidate_for_rect[0], candidate_for_rect[1], candidate_for_rect[2]
            )
            rect = make_rect_with_triangle(tri)
            if not rect.is_valid:
                continue

            self.rect1 = rect
            self.second_rect_point = point
            for candidate in candidate_for_rect:
                if point.x == candidate.x and point.y == candidate.y:
                    self.is_rectangular_prism = True
                elif point.y == candidate.y and point.z == candidate.z:
                    self.is_rectangular_prism = True
                elif point.x == candidate.x and point.z == candidate.z:
                    self.is_rectangular_prism = True

    def calculate_is_cube(self) -> None:
        if not self.is_rectangular_prism:
            self.is_cube = False

        if not self.rect1.is_square:
            self.is_cube = False

        d = self.rect1.a.get_distance_to(self.rect1.b)
        for point in [self.a, self.b, self.c, self.d]:
            if point is self.second_rect_point:
                continue

            if (
                point.x == self.second_rect_point.x
                and point.y == self.second_rect_point.y
            ):
                self.is_cube = d - self.second_rect_point.get_distance_to(point) < self.DISTANCE_ERROR_TOLARANCE
                return
            elif (
                point.y == self.second_rect_point.y
                and point.z == self.second_rect_point.z
            ):
                self.is_cube = d - self.second_rect_point.get_distance_to(point) < self.DISTANCE_ERROR_TOLARANCE
                return
            elif (
                point.x == self.second_rect_point.x
                and point.z == self.second_rect_point.z
            ):
                self.is_cube = d - self.second_rect_point.get_distance_to(point) < self.DISTANCE_ERROR_TOLARANCE
                return
        self.is_cube = False

    def is_point_inside(self, x: Point3d) -> bool:
        return False
