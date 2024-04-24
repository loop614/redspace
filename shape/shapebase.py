from __future__ import annotations

from primary.point import Point


class ShapeBase:
    def separate_points_per_planes(self, points: list[Point]):
        is_valid = False
        polygon1_points = []
        second_polygon_point = None
        second_polygon_point_bellow = None

        for point in reversed(points):
            candidate_for_rect = []
            for point2 in points:
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

            polygon1_points = candidate_for_rect
            second_polygon_point = point
            for candidate in candidate_for_rect:
                if (
                    second_polygon_point.x == candidate.x
                    and second_polygon_point.y == candidate.y
                ):
                    second_polygon_point_bellow = candidate
                    is_valid = True
                    break
                elif (
                    second_polygon_point.y == candidate.y
                    and second_polygon_point.z == candidate.z
                ):
                    second_polygon_point_bellow = candidate
                    is_valid = True
                    break
                elif (
                    second_polygon_point.x == candidate.x
                    and second_polygon_point.z == candidate.z
                ):
                    second_polygon_point_bellow = candidate
                    is_valid = True
                    break

            if is_valid:
                break

        return (is_valid, polygon1_points, second_polygon_point, second_polygon_point_bellow)
