# Classes
#   - Data Classes

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, obj):
        return self.x == obj.x and self.y == obj.y

p1 = Point(1, 2)
p2 = Point(1, 2)

print(p1 == p2) #false before implementing __eq__
print(id(p1))
print(id(p2))


from collections import namedtuple


Point2 = namedtuple("Point2", ["x", "y"])
p10 = Point2(1, 2)
p20 = Point2(1, 2)
print(p10 == p20)