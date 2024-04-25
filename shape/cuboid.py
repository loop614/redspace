from __future__ import annotations

from decimal import Decimal

from figure.quad import make_quad_with_triangle
from figure.quad import Quad
from figure.triangle import Triangle
from primary.distance import Distance
from primary.vector import Vector
from redlogger import redlog
from shape.shapebase import ShapeBase


class Cuboid(ShapeBase):
    quadhorz1: Quad
    quadhorz2: Quad
    height: Distance
    is_valid: bool
    is_rectangular_prism: bool
    is_cube: bool
    spational_diagonal: Distance
    second_quad_point: Vector
    second_quad_point_bellow: Vector

    def __init__(self, a: Vector, b: Vector, c: Vector, d: Vector) -> None:
        super().__init__()
        points = [a, b, c, d]
        self.is_valid = False
        self.is_rectangular_prism = False
        self.is_cube = False
        self.calculate_is_rectangular_prism(points)
        self.calculate_height()
        self.calculate_is_cube()
        self.calculate_diagonal()
        self.calculate_quadhorz2()

    def calculate_is_rectangular_prism(self, points_for_cuboid: list[Vector]) -> None:
        polygon1_points = []
        (self.is_valid, polygon1_points, self.second_quad_point, self.second_quad_point_bellow) = (
            self.separate_points_per_planes(points_for_cuboid)
        )
        if not self.is_valid:
            return

        tri = Triangle(
            polygon1_points[0],
            polygon1_points[1],
            polygon1_points[2],
        )
        self.quadhorz1 = make_quad_with_triangle(tri)
        redlog(f'self.quadhorz1 is {self.quadhorz1}')
        self.is_rectangular_prism = self.quadhorz1.is_rect

    def calculate_height(self) -> None:
        for point in self.quadhorz1.get_points():
            if (
                point.x == self.second_quad_point.x
                and point.y == self.second_quad_point.y
            ):
                self.height = self.second_quad_point.get_distance_to(point)
                return
            elif (
                point.y == self.second_quad_point.y
                and point.z == self.second_quad_point.z
            ):
                self.height = self.second_quad_point.get_distance_to(point)
                return
            elif (
                point.x == self.second_quad_point.x
                and point.z == self.second_quad_point.z
            ):
                self.height = self.second_quad_point.get_distance_to(point)
                return

    def calculate_is_cube(self) -> None:
        if not self.quadhorz1.is_square:
            self.is_cube = False
            return

        self.is_cube = self.quadhorz1.sideab.is_equal(self.height)

    def calculate_diagonal(self) -> None:
        self.spational_diagonal = Distance(
            (
                self.quadhorz1.sideab.val**2
                + self.quadhorz1.sidebc.val**2
                + self.height.val**2
            ).sqrt(),
        )

    def calculate_quadhorz2(self) -> None:
        linepoints = []
        for point in self.quadhorz1.get_points():
            if self.second_quad_point_bellow is point:
                continue
            if (
                self.second_quad_point_bellow.x == point.x
                and self.second_quad_point_bellow.y == point.y
            ):
                linepoints.append(point)
            elif (
                self.second_quad_point_bellow.y == point.y
                and self.second_quad_point_bellow.z == point.z
            ):
                linepoints.append(point)
            elif (
                self.second_quad_point_bellow.x == point.x
                and self.second_quad_point_bellow.z == point.z
            ):
                linepoints.append(point)

        if len(linepoints) != 2:
            redlog('could not calculate quad horizontal 2 for cuboid')
            return

        quadhorz1 = make_quad_with_triangle(
            Triangle(
                self.second_quad_point,
                self.second_quad_point_bellow,
                linepoints[0],
            ),
        )

        quadhorz2 = make_quad_with_triangle(
            Triangle(
                self.second_quad_point,
                self.second_quad_point_bellow,
                linepoints[1],
            ),
        )
        self.quadhorz2 = make_quad_with_triangle(
            Triangle(quadhorz1.d, quadhorz2.d, self.second_quad_point),
        )
        redlog(f'self.quadhorz2 is {self.quadhorz2}')

    def is_point_inside(self, point: Vector):
        """
        https://math.stackexchange.com/questions/1472049/check-if-a-point-is-inside-a-rectangular-shaped-area-3d
        """
        other_two_points: list[Vector] = []
        for point in self.quadhorz1.get_points():
            if (
                point is not self.second_quad_point
                and point is not self.second_quad_point_bellow
            ):
                other_two_points.append(point)

        p1: Vector = self.second_quad_point_bellow
        p5: Vector = self.second_quad_point
        p2: Vector = other_two_points[0]
        p4: Vector = other_two_points[1]

        i: Vector = p1 - p2
        j: Vector = p1 - p4
        k: Vector = p1 - p5
        v: Vector = p1 - point

        vi: Decimal = v.dot(i)
        vj: Decimal = v.dot(j)
        vk: Decimal = v.dot(k)

        return (
            0 < vi and vi < i.dot(i) and
            0 < vj and vj < j.dot(j) and
            0 < vk and vk < k.dot(k)
        )
