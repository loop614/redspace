from __future__ import annotations

from figure.quad import make_quad_with_triangle
from figure.quad import Quad
from figure.triangle import Triangle
from primary.distance import Distance
from primary.point import Point
from primary.vector import make_vector_from_points
from primary.vector import Vector


class Cuboid:
    quadhorz1: Quad
    quadhorz2: Quad
    position1: Vector
    position2: Vector
    position3: Vector
    is_rectangular_prism: bool
    is_cube: bool
    spational_diagonal: Distance
    second_quad_point: Point
    second_quad_point_bellow: Point
    second_quad_side: Distance

    def __init__(self, a: Point, b: Point, c: Point, d: Point) -> None:
        points = [a, b, c, d]
        self.calculate_is_rectangular_prism(points)
        self.calculate_is_cube()
        self.calculate_diagonal()

    def calculate_is_rectangular_prism(self, points_for_cuboid: list[Point]) -> None:
        self.is_rectangular_prism = False
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
            self.quadhorz1 = make_quad_with_triangle(tri)
            if not self.quadhorz1.is_rect:
                continue

            self.second_quad_point = point
            for candidate in candidate_for_rect:
                if point.x == candidate.x and point.y == candidate.y:
                    self.second_quad_point_bellow = candidate
                    self.is_rectangular_prism = True
                    break
                elif point.y == candidate.y and point.z == candidate.z:
                    self.second_quad_point_bellow = candidate
                    self.is_rectangular_prism = True
                    break
                elif point.x == candidate.x and point.z == candidate.z:
                    self.second_quad_point_bellow = candidate
                    self.is_rectangular_prism = True
                    break

    def calculate_is_cube(self) -> None:
        if not self.is_rectangular_prism:
            self.is_cube = False

        if not self.quadhorz1.is_square:
            self.is_cube = False

        d = self.quadhorz1.a.get_distance_to(self.quadhorz1.b)
        for point in self.quadhorz1.get_points():
            if (
                point.x == self.second_quad_point.x
                and point.y == self.second_quad_point.y
            ):
                self.second_quad_side = self.second_quad_point.get_distance_to(
                    point,
                )
                self.is_cube = d.is_equal(self.second_quad_side)
                return
            elif (
                point.y == self.second_quad_point.y
                and point.z == self.second_quad_point.z
            ):
                self.second_quad_side = self.second_quad_point.get_distance_to(
                    point,
                )
                self.is_cube = d.is_equal(self.second_quad_side)
                return
            elif (
                point.x == self.second_quad_point.x
                and point.z == self.second_quad_point.z
            ):
                self.second_quad_side = self.second_quad_point.get_distance_to(
                    point,
                )
                self.is_cube = d.is_equal(self.second_quad_side)
                return
        self.is_cube = False

    def calculate_diagonal(self) -> None:
        self.spational_diagonal = Distance(
            (
                self.quadhorz1.sideab.val**2
                + self.quadhorz1.sidebc.val**2
                + self.second_quad_side.val**2
            ).sqrt(),
        )

    def is_point_inside(self, x: Point) -> bool:
        other_two_points: list[Point] = []
        for point in self.quadhorz1.get_points():
            if (
                point is not self.second_quad_point
                and point is not self.second_quad_point_bellow
            ):
                other_two_points.append(point)

        p1 = self.second_quad_point_bellow
        p5 = self.second_quad_point
        p2 = other_two_points[0]
        p4 = other_two_points[1]

        self.position1 = make_vector_from_points(p1, p4).cross(
            make_vector_from_points(p1, p5),
        )
        self.position2 = make_vector_from_points(p1, p2).cross(
            make_vector_from_points(p1, p5),
        )
        self.position3 = make_vector_from_points(p1, p2).cross(
            make_vector_from_points(p1, p4),
        )

        return False
