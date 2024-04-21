from figures.point2d import Point2d
from figures.rect import Rect, make_rect_with_triangle
from figures.triangle import Triangle


def solve(points: list[Point2d]):
    if len(points) != 4:
        print("ERROR: Expected to find 4 points for solving the task")
        return

    tri: Triangle = Triangle(points[0], points[1], points[2])
    x: Point2d = points[3]

    tri.calculate_sides()
    tri.calculate_angles()
    rect = make_rect_with_triangle(tri)

    if not rect.is_valid_tri():
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
