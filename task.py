from figures.point2d import Point2d
from figures.rect import Rect, make_rect_with_3_points


def solve(points: list[Point2d]):
    if len(points) != 4:
        print("ERROR: Expected to find 4 points for solving the task")
        return

    rect: Rect = make_rect_with_3_points(points[0], points[1], points[2])
    x: Point2d = points[3]

    if not rect.is_valid():
        print("false")
        print("ERROR task: Could not make a rectangle from given points")
        return

    print("true")
    print("INFO: Rectangle found")

    if rect.is_point_inside(x):
        print(f"Point {x} is in Rectangle\n{rect}")
    else:
        print(f"Point {x} is not in Rectangle\n{rect}")

    print(f"Diagnoal lenght {rect.diaginal_len}")
