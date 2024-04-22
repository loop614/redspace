from primary.point3d import Point3d
from figure3d.polygon import Polygon


def solve(points: list[Point3d]):
    if len(points) < 6:
        print("ERROR: Expected to find more than 5 points for solving the universal polygon")
        return

    poly: Polygon = Polygon()
    x: Point3d = points[-1]
    unsorted_points = points[:1]
