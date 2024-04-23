from __future__ import annotations

from figure.quad import make_quad_with_triangle
from figure.triangle import Triangle
from primary.point import Point
from redlogger import redlog


def solve(points: list[Point]) -> int:
    if len(points) != 4:
        redlog('ERROR: Expected to find 4 points for solving the task')
        return 1

    tri: Triangle = Triangle(points[0], points[1], points[2])
    x: Point = points[3]
    quad = make_quad_with_triangle(tri)

    if not quad.is_rect:
        redlog('false', force=True)
        redlog('ERROR task: Could not make a rectangle from given points')
        return 1

    redlog('true', force=True)
    redlog('INFO: Rectangle found')

    if quad.is_point_inside(x):
        redlog(f'Point {x} is in Rectangle\n{quad}')
    else:
        redlog(f'Point {x} is not in Rectangle\n{quad}')

    redlog(f'Diagnoal lenght {quad.diaginal_len}')
    return 0
