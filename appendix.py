from figures.cuboid import Cuboid, make_cuboid_with_4_points
from figures.point3d import Point3d


def solve(points: list[Point3d]):
    if len(points) != 5:
        print("ERROR: Expected to find 5 points for solving the appendix")
        return

    c: Cuboid = make_cuboid_with_4_points(points[0], points[1], points[2], points[3])
    x: Point3d = points[4]
    if c.is_rectangular_prism():
        print("it is_rectangular_prism")

    if c.is_cube():
        print("it is_cube")
    else:
        print("it is not a cube")

    if c.is_point_inside(x):
        print(f"True")
        print(f"x = {x} is inside of cuboid")
    else:
        print(f"False")
        print(f"x = {x} is not inside of cuboid")
