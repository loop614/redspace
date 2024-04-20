import os

from figures.point2d import Point2d
from figures.point3d import Point3d
from task import solve as tasksolver
from appendix import solve as appendixsolver


def readfile(file_path: str) -> None:
    file_of_two_d = False
    file_of_three_d = False
    points2d = []
    points3d = []

    with open(file_path, "r") as file:
        for line in file.readlines():
            numbers = line.strip().split(",")
            curr2Point = None
            curr3Point = None
            if len(numbers) == 2 and not file_of_three_d:
                curr2Point = Point2d(float(numbers[0]), float(numbers[1]))
                file_of_two_d = True
                points2d.append(curr2Point)
            elif len(numbers) == 3 and not file_of_two_d:
                curr3Point = Point3d(float(numbers[0]), float(numbers[1]), float(numbers[2]))
                file_of_three_d = True
                points3d.append(curr3Point)
            else:
                print(
                    "File not in expected format. Skipping line.",
                    "Please provide file with 2 or 3 comma seprated numbers in line, with 4 or 5 lines"
                )
                continue

        if file_of_two_d:
            tasksolver(points2d)
        elif file_of_three_d:
            appendixsolver(points3d)


def main():
    for task1file in os.listdir("taskfiles"):
        if task1file.endswith(".txt"):
            print(task1file)
            readfile(os.path.join("taskfiles", task1file))
            print("")

    for appendixfile in os.listdir("appendixfiles"):
        if appendixfile.endswith(".txt"):
            print(appendixfile)
            readfile(os.path.join("appendixfiles", appendixfile))
            print("")


if __name__ == "__main__":
    raise SystemExit(main())
