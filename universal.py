from __future__ import annotations

from primary.vector import Vector
from redlogger import redlog
from shape.anyshape import AnyShape


def solve(points: list[Vector]) -> int:
    if len(points) < 6:
        redlog(
            'ERROR: Expected to find more than 5 points for solving the universal anyshape',
        )
        return 1

    anyshp: AnyShape = AnyShape(points[:-1])
    if anyshp.is_valid:
        redlog(
            'provided points can make a anyshape. Assuming points come in order of connection',
        )
        redlog(f'spational diagonal = {anyshp.spational_diagonal}')
    else:
        redlog('could not make a anyshape from provided points')
        return 1

    if anyshp.are_all_sides_equal:
        redlog('anyshape has all sides equal')
    else:
        redlog('anyshape has not all sides equal')

    x: Vector = points[-1]
    if anyshp.is_point_inside(x):
        redlog(f'{x} is in the anyshape')
    else:
        redlog(f'{x} is not in the anyshape')

    return 0
