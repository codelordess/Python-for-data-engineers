from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p1 = Point(x=1, y=2)
p2 = Point(x=3, y=4)
print(p1 == p2)

# Creating a named tuple to represent a point in 2D space