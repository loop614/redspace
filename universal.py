from __future__ import annotations

from figure3d.polygon import Polygon
from primary.point import Point


def solve(points: list[Point]):
    if len(points) < 6:
        print(
            'ERROR: Expected to find more than 5 points for solving the universal polygon',
        )
        return

    poly: Polygon = Polygon()
    x: Point = points[-1]
    unsorted_points = points[:1]
