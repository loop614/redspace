from __future__ import annotations

from figure3d.figure3dbase import Figure3d
from primary.point import Point


class Polygon(Figure3d):
    points: list[Point]
    shape1_points: list[Point]
    shape2_points: list[Point]
    second_shape_point: Point

    def is_polygon(self) -> bool:
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

            self.shape1_points = candidate_for_rect
            self.second_shape_point = point
            for candidate in candidate_for_rect:
                if point.x == candidate.x and point.y == candidate.y:
                    return True
                elif point.y == candidate.y and point.z == candidate.z:
                    return True
                elif point.x == candidate.x and point.z == candidate.z:
                    return True

        return False
