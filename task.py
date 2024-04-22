from __future__ import annotations

from figure.quad import make_quad_with_triangle
from figure.triangle import Triangle
from primary.point import Point


def solve(points: list[Point]):
    if len(points) != 4:
        print('ERROR: Expected to find 4 points for solving the task')
        return

    tri: Triangle = Triangle(points[0], points[1], points[2])
    x: Point = points[3]
    quad = make_quad_with_triangle(tri)

    if not quad.is_rect:
        print('false')
        print('ERROR task: Could not make a rectangle from given points')
        return

    print('true')
    print('INFO: Rectangle found')

    if quad.is_point_inside(x):
        print(f'Point {x} is in Rectangle\n{quad}')
    else:
        print(f'Point {x} is not in Rectangle\n{quad}')

    print(f'Diagnoal lenght {quad.diaginal_len}')
