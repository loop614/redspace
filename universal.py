from __future__ import annotations

from primary.point import Point
from shape.anyshape import AnyShape


def solve(points: list[Point]):
    if len(points) < 6:
        print(
            'ERROR: Expected to find more than 5 points for solving the universal anyshape',
        )
        return

    poly: AnyShape = AnyShape(points[:-1])
    if poly.is_valid:
        print('provided points can make a anyshape. Assuming points come in order of connection')
        print(f'spational diagonal = {poly.spational_diagonal}')
    else:
        print('could not make a anyshape from provided points')
        return

    if poly.are_all_sides_equal:
        print('anyshape has all sides equal')
    else:
        print('anyshape has not all sides equal')

    x: Point = points[-1]
    if poly.is_point_inside(x):
        print(f'{x} is in the anyshape')
    else:
        print(f'{x} is not in the anyshape')
