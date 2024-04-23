from __future__ import annotations

from primary.point import Point
from redlogger import redlog
from shape.cuboid import Cuboid


def solve(points: list[Point]) -> int:
    if len(points) != 5:
        redlog('ERROR: Expected to find 5 points for solving the appendix')
        return 1

    c: Cuboid = Cuboid(points[0], points[1], points[2], points[3])
    x: Point = points[4]
    if c.is_rectangular_prism:
        redlog('it is_rectangular_prism')
        redlog(f'spational diagonal = {c.spational_diagonal}')
    else:
        redlog('it is not a rectangular_prism')
        redlog(
            'please provide 3 points from one rectangle and one point from another cuboid rectangle',
        )
        return 1

    if c.is_cube:
        redlog('it is_cube')
    else:
        redlog('it is not a cube')

    if c.is_point_inside(x):
        redlog('True', force=True)
        redlog(f'x = {x} is inside of cuboid')
    else:
        redlog('False', force=True)
        redlog(f'x = {x} is not inside of cuboid')

    return 0
