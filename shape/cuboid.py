from __future__ import annotations

import numpy as np

from figure.quad import make_quad_with_triangle
from figure.quad import Quad
from figure.triangle import Triangle
from primary.distance import Distance
from primary.point import Point
from primary.vector import Vector
from redlogger import redlog


class Cuboid:
    quadhorz1: Quad
    quadhorz2: Quad
    height: Distance
    position1: Vector
    position2: Vector
    position3: Vector
    is_rectangular_prism: bool
    is_cube: bool
    spational_diagonal: Distance
    second_quad_point: Point
    second_quad_point_bellow: Point

    def __init__(self, a: Point, b: Point, c: Point, d: Point) -> None:
        points = [a, b, c, d]
        self.is_rectangular_prism = False
        self.is_cube = False
        self.calculate_is_rectangular_prism(points)
        self.calculate_height()
        self.calculate_is_cube()
        self.calculate_diagonal()
        self.calculate_quadhorz2()

    def calculate_is_rectangular_prism(self, points_for_cuboid: list[Point]) -> None:
        self.is_rectangular_prism = False
        point_to_skip = len(points_for_cuboid) - 1
        for point in points_for_cuboid:
            candidate_for_rect = []
            for j, point2 in enumerate(points_for_cuboid):
                if j != point_to_skip:
                    candidate_for_rect.append(point2)
            point_to_skip -= 1
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
            redlog(f'self.quadhorz1 is {self.quadhorz1}')
            if not self.quadhorz1.is_rect:
                continue

            self.second_quad_point = points_for_cuboid[point_to_skip+1]
            for candidate in candidate_for_rect:
                if self.second_quad_point.x == candidate.x and self.second_quad_point.y == candidate.y:
                    self.second_quad_point_bellow = candidate
                    self.is_rectangular_prism = True
                    break
                elif self.second_quad_point.y == candidate.y and self.second_quad_point.z == candidate.z:
                    self.second_quad_point_bellow = candidate
                    self.is_rectangular_prism = True
                    break
                elif self.second_quad_point.x == candidate.x and self.second_quad_point.z == candidate.z:
                    self.second_quad_point_bellow = candidate
                    self.is_rectangular_prism = True
                    break
            break

    def calculate_height(self) -> None:
        for point in self.quadhorz1.get_points():
            if (
                point.x == self.second_quad_point.x
                and point.y == self.second_quad_point.y
            ):
                self.height = self.second_quad_point.get_distance_to(
                    point,
                )
                return
            elif (
                point.y == self.second_quad_point.y
                and point.z == self.second_quad_point.z
            ):
                self.height = self.second_quad_point.get_distance_to(
                    point,
                )
                return
            elif (
                point.x == self.second_quad_point.x
                and point.z == self.second_quad_point.z
            ):
                self.height = self.second_quad_point.get_distance_to(
                    point,
                )
                return

    def calculate_is_cube(self) -> None:
        if not self.is_rectangular_prism:
            self.is_cube = False
            return

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
            if self.second_quad_point_bellow.x == point.x and self.second_quad_point_bellow.y == point.y:
                linepoints.append(point)
            elif self.second_quad_point_bellow.y == point.y and self.second_quad_point_bellow.z == point.z:
                linepoints.append(point)
            elif self.second_quad_point_bellow.x == point.x and self.second_quad_point_bellow.z == point.z:
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

    def is_point_inside(self, point: Point):
        prism = self.quadhorz1.get_points() + self.quadhorz2.get_points()

        def is_inside_bbox(point, bbox):
            x, y, z = point.x, point.y, point.z
            (x1, y1, z1), (x2, y2, z2) = bbox
            return x1 <= x <= x2 and y1 <= y <= y2 and z1 <= z <= z2

        # Create a bounding box for the prism
        x_coords = [vertex.x for vertex in prism]
        y_coords = [vertex.y for vertex in prism]
        z_coords = [vertex.z for vertex in prism]

        bbox = (
            (min(x_coords), min(y_coords), min(z_coords)),
            (max(x_coords), max(y_coords), max(z_coords)),
        )

        # Check if the point is inside the bounding box
        if not is_inside_bbox(point, bbox):
            return False

        # Check if the point is inside the prism
        faces = [
            [prism[0], prism[1], prism[2], prism[3]],
            [prism[4], prism[5], prism[6], prism[7]],
            [prism[0], prism[1], prism[5], prism[4]],
            [prism[2], prism[3], prism[7], prism[6]],
            [prism[0], prism[3], prism[7], prism[4]],
            [prism[1], prism[2], prism[6], prism[5]],
        ]

        for face in faces:
            A = (face[0].x, face[0].y, face[0].z)
            B = (face[1].x, face[1].y, face[1].z)
            C = (face[2].x, face[2].y, face[2].z)
            normal = np.cross(
                np.array(B) - np.array(A),
                np.array(C) - np.array(A),
            )
            point_vector = np.array((point.x, point.y, point.z)) - np.array(A)

            if np.dot(normal, point_vector) > 0:
                return False

        return True
