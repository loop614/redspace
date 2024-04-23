from __future__ import annotations

from decimal import Decimal

from primary.distance import Distance
from primary.point import Point


class AnyShape:
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
        self.points = points
        self.spational_diagonal = Distance(Decimal(0))
        self.are_all_sides_equal = False
        self.is_valid = False
        self.polygon1_sides = []
        self.is_polygon()
        self.calculate_sides()
        self.calculate_diagonal()

    def is_polygon(self) -> None:
        for point in self.points:
            candidate_for_rect = []
            for point2 in self.points:
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

            self.polygon1_points = candidate_for_rect
            self.second_polygon_point = point
            for candidate in candidate_for_rect:
                if point.x == candidate.x and point.y == candidate.y:
                    self.second_polygon_point_bellow = candidate
                    self.is_valid = True
                    break
                elif point.y == candidate.y and point.z == candidate.z:
                    self.second_polygon_point_bellow = candidate
                    self.is_valid = True
                    break
                elif point.x == candidate.x and point.z == candidate.z:
                    self.second_polygon_point_bellow = candidate
                    self.is_valid = True
                    break

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
