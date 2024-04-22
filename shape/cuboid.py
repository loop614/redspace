from __future__ import annotations

from figure.quad import make_quad_with_triangle
from figure.quad import Quad
from figure.triangle import Triangle
from primary.distance import Distance
from primary.point import Point
from primary.vector import make_vector_from_points
from primary.vector import Vector


class Cuboid:
    a: Point
    b: Point
    c: Point
    d: Point
    u: Vector
    v: Vector
    w: Vector
    quad1: Quad
    is_rectangular_prism: bool
    is_cube: bool
    spational_diagonal: Distance
    second_rect_point: Point
    second_rect_point_bellow: Point
    second_rect_side: Distance

    def __init__(self, a: Point, b: Point, c: Point, d: Point) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.calculate_is_rectangular_prism()
        self.calculate_is_cube()
        self.calculate_diagonal()

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
                candidate_for_rect[0],
                candidate_for_rect[1],
                candidate_for_rect[2],
            )
            self.quad1 = make_quad_with_triangle(tri)
            if not self.quad1.is_rect:
                continue

            self.second_rect_point = point
            for candidate in candidate_for_rect:
                if point.x == candidate.x and point.y == candidate.y:
                    self.second_rect_point_bellow = candidate
                    self.is_rectangular_prism = True
                    break
                elif point.y == candidate.y and point.z == candidate.z:
                    self.second_rect_point_bellow = candidate
                    self.is_rectangular_prism = True
                    break
                elif point.x == candidate.x and point.z == candidate.z:
                    self.second_rect_point_bellow = candidate
                    self.is_rectangular_prism = True
                    break

    def calculate_is_cube(self) -> None:
        if not self.is_rectangular_prism:
            self.is_cube = False

        if not self.quad1.is_square:
            self.is_cube = False

        d = self.quad1.a.get_distance_to(self.quad1.b)
        for point in [self.a, self.b, self.c, self.d]:
            if point is self.second_rect_point:
                continue

            if (
                point.x == self.second_rect_point.x
                and point.y == self.second_rect_point.y
            ):
                self.second_rect_side = self.second_rect_point.get_distance_to(
                    point,
                )
                self.is_cube = d.is_equal(self.second_rect_side)
                return
            elif (
                point.y == self.second_rect_point.y
                and point.z == self.second_rect_point.z
            ):
                self.second_rect_side = self.second_rect_point.get_distance_to(
                    point,
                )
                self.is_cube = d.is_equal(self.second_rect_side)
                return
            elif (
                point.x == self.second_rect_point.x
                and point.z == self.second_rect_point.z
            ):
                self.second_rect_side = self.second_rect_point.get_distance_to(
                    point,
                )
                self.is_cube = d.is_equal(self.second_rect_side)
                return
        self.is_cube = False

    def calculate_diagonal(self) -> None:
        self.spational_diagonal = Distance(
            (
                self.quad1.sideab.val**2
                + self.quad1.sidebc.val**2
                + self.second_rect_side.val**2
            ).sqrt(),
        )

    def is_point_inside(self, x: Point) -> bool:
        other_two_points: list[Point] = []
        for point in [self.a, self.b, self.c, self.d]:
            if (
                point is not self.second_rect_point
                and point is not self.second_rect_point_bellow
            ):
                other_two_points.append(point)

        # https://math.stackexchange.com/questions/1472049/check-if-a-point-is-inside-a-rectangular-shaped-area-3d
        p1 = self.second_rect_point_bellow
        p5 = self.second_rect_point
        p2 = other_two_points[0]
        p4 = other_two_points[1]

        self.u = make_vector_from_points(p1, p4).cross(
            make_vector_from_points(p1, p5),
        )
        self.v = make_vector_from_points(p1, p2).cross(
            make_vector_from_points(p1, p5),
        )
        self.w = make_vector_from_points(p1, p2).cross(
            make_vector_from_points(p1, p4),
        )

        return False
