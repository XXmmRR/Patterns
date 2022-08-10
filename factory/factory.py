from enum import Enum
from math import *


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    class PointFactory:
        @staticmethod
        def new_cartesian_point(x, y):
            return Point(x, y)

        @staticmethod
        def new_polar_point(rho, theta):
            return Point(rho * cos(theta), rho * sin(theta))

    def __str__(self):
        return str(self.x) + str(self.y)


if __name__ == '__main__':
    p = Point(2, 3)
    p2 = Point.new_cartesian_point(1, 2)
    print(p2)
