from __future__ import annotations

from primary.point import Point
from shape.cuboid import Cuboid


def solve(points: list[Point]):
    if len(points) != 5:
        print('ERROR: Expected to find 5 points for solving the appendix')
        return

    c: Cuboid = Cuboid(points[0], points[1], points[2], points[3])
    x: Point = points[4]
    if c.is_rectangular_prism:
        print('it is_rectangular_prism')
        print(f'spational diagonal = {c.spational_diagonal}')
    else:
        print('it is not a rectangular_prism')
        print('please provide 3 points from one rectangle and one point from another cuboid rectangle')
        return

    if c.is_cube:
        print('it is_cube')
    else:
        print('it is not a cube')

    if c.is_point_inside(x):
        print('True')
        print(f'x = {x} is inside of cuboid')
    else:
        print('False')
        print(f'x = {x} is not inside of cuboid')
