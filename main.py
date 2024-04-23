from __future__ import annotations

import os
import sys
from decimal import Decimal

from appendix import solve as appendixsolver
from primary.point import Point
from redlogger import redlog
from redlogger import turnLoggerOn
from task import solve as tasksolver
from universal import solve as anyshapesolver


def solvefile(file_path: str) -> int:
    res: int = 0
    file_of_two_d = False
    file_of_three_d = False
    points2d = []
    points3d = []

    with open(file_path) as file:
        for line in file.readlines():
            numbers = line.strip().split(',')
            if len(numbers) == 2 and not file_of_three_d:
                curr2Point = Point(
                    Decimal(numbers[0]),
                    Decimal(numbers[1]),
                )
                file_of_two_d = True
                points2d.append(curr2Point)
            elif len(numbers) == 3 and not file_of_two_d:
                curr3Point = Point(
                    Decimal(numbers[0]),
                    Decimal(numbers[1]),
                    Decimal(numbers[2]),
                )
                file_of_three_d = True
                points3d.append(curr3Point)
            else:
                redlog(
                    'File in unexpected format. Skipping line.',
                    'Please provide file with 2 or 3 comma seprated numbers in line, with 4 or more lines',
                )

        if file_of_two_d:
            res |= tasksolver(points2d)
        elif file_of_three_d and len(points3d) <= 5:
            res |= appendixsolver(points3d)
        elif file_of_three_d and len(points3d) > 5:
            res |= anyshapesolver(points3d)

    return res


def main(extrafiles: bool = False) -> int:
    res: int = 0
    if not extrafiles:
        res |= solvefile(os.path.join('taskfiles', 'input1.txt'))
        res |= solvefile(os.path.join('appendixfiles', 'input2.txt'))
        return res

    for task1file in os.listdir('taskfiles'):
        if task1file.endswith('.txt'):
            redlog(task1file)
            res |= solvefile(os.path.join('taskfiles', task1file))
            redlog('')

    for appendixfile in os.listdir('appendixfiles'):
        if appendixfile.endswith('.txt'):
            redlog(appendixfile)
            res |= solvefile(os.path.join('appendixfiles', appendixfile))
            redlog('')

    return res


if __name__ == '__main__':
    debug = False
    extrafiles = False
    for arg in sys.argv:
        if arg == '--debug':
            turnLoggerOn()
        elif arg == '--extrafiles':
            extrafiles = True

    raise SystemExit(main(extrafiles))
