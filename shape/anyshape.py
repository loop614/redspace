from __future__ import annotations

from decimal import Decimal

from primary.distance import Distance
from primary.point import Point
from shape.shapebase import ShapeBase


class AnyShape(ShapeBase):
    points: list[Point]
    polygon1_points: list[Point]
    polygon2_points: list[Point]
    polygon1_sides: list[Distance]
    is_valid: bool
    spational_diagonal: Distance
    second_polygon_point: Point
    second_polygon_point_bellow: Point
    second_polygon_side: Distance
    are_all_sides_equal: bool

    def __init__(self, points: list[Point]) -> None:
        super().__init__()
        self.points = points
        self.spational_diagonal = Distance(Decimal(0))
        self.are_all_sides_equal = False
        self.is_valid = False
        self.polygon1_sides = []
        self.calculate_is_polygon()
        self.calculate_sides()
        self.calculate_diagonal()

    def calculate_is_polygon(self) -> None:
        (self.is_valid, self.polygon1_points, self.second_polygon_point, self.second_polygon_point_bellow) = (
            self.separate_points_per_planes(self.points)
        )

    def calculate_sides(self) -> None:
        d = self.points[0].get_distance_to(self.points[1])
        self.are_all_sides_equal = True
        self.second_polygon_side = self.second_polygon_point.get_distance_to(
            self.second_polygon_point_bellow,
        )
        if d != self.second_polygon_side:
            self.are_all_sides_equal = False

        for index, point in enumerate(self.points):
            next_one = index + 1
            if next_one == len(self.points):
                next_one = 0

            curr = point.get_distance_to(self.points[next_one])
            if d != curr:
                self.are_all_sides_equal = False

            self.polygon1_sides.append(curr)

    def calculate_diagonal(self) -> None:
        pass

    def is_point_inside(self, point: Point) -> bool:
        return False
