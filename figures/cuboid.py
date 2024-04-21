from figures.point2d import Point2d
from figures.point3d import Point3d
from figures.rect import Rect, make_rect_with_triangle
from figures.triangle import Triangle


class Cuboid:
    a: Point3d
    b: Point3d
    c: Point3d
    d: Point3d
    rect1: Rect
    second_rect_point: Point3d

    def is_rectangular_prism(self) -> bool:
        points_for_cuboid = [self.a, self.b, self.c, self.d]
        for point in points_for_cuboid:
            candidate_for_rect = []
            self.second_rect_point = point
            for point2 in points_for_cuboid:
                if point is not point2:
                    candidate_for_rect.append(point2)

            xpivot = candidate_for_rect[0].x
            ypivot = candidate_for_rect[0].y
            zpivot = candidate_for_rect[0].z
            x_same = y_same = z_same = True

            for candidate in candidate_for_rect[1:]:
                if xpivot != candidate.x:
                    x_same = False
                if ypivot != candidate.y:
                    y_same = False
                if zpivot != candidate.z:
                    z_same = False

            if not x_same and not y_same and not z_same:
                continue

            list2dcandidates: list[Point2d] = []
            for candidate in candidate_for_rect:
                if x_same:
                    list2dcandidates.append(Point2d(candidate.y, candidate.z))
                elif y_same:
                    list2dcandidates.append(Point2d(candidate.x, candidate.z))
                elif z_same:
                    list2dcandidates.append(Point2d(candidate.x, candidate.y))

            tri = Triangle(list2dcandidates[0], list2dcandidates[1], list2dcandidates[2])
            tri.calculate_sides()
            tri.calculate_angles()
            rect = make_rect_with_triangle(tri)
            if not rect.is_valid_tri():
                continue

            self.rect1 = rect
            for candidate in candidate_for_rect:
                if point.x == candidate.x and point.y == candidate.y:
                    return True
                elif point.y == candidate.y and point.z == candidate.z:
                    return True
                elif point.x == candidate.x and point.z == candidate.z:
                    return True

        return False


    def is_cube(self) -> bool:
        if not self.rect1.is_square:
            return False

        d = self.rect1.a.get_distance_to(self.rect1.b)
        for point in [self.a, self.b, self.c, self.d]:
            if point is self.second_rect_point:
                continue

            if point.x == self.second_rect_point.x and point.y == self.second_rect_point.y:
                return d == self.second_rect_point.get_distance_to(point)
            elif point.y == self.second_rect_point.y and point.z == self.second_rect_point.z:
                return d == self.second_rect_point.get_distance_to(point)
            elif point.x == self.second_rect_point.x and point.z == self.second_rect_point.z:
                return d == self.second_rect_point.get_distance_to(point)
        return False


    def is_point_inside(self, x: Point3d) -> bool:
        return False


def make_cuboid_with_4_points(a: Point3d, b: Point3d, c: Point3d, d: Point3d):
    cb = Cuboid()
    cb.a = a
    cb.b = b
    cb.c = c
    cb.d = d

    return cb
