import math


class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if isinstance(value, (int, float)):
            self._x = value
        else:
            raise ValueError("Координата x должна быть числом")

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if isinstance(value, (int, float)):
            self._y = value
        else:
            raise ValueError("Координата y должна быть числом")

    def distance_to(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


point1 = Point(2, 3)
point2 = Point(5, 7)

print("Координаты точки 1:", (point1.x, point1.y))
print("Координаты точки 2:", (point2.x, point2.y))

distance = point1.distance_to(point2)
print("Расстояние между точкой 1 и точкой 2:", distance)

