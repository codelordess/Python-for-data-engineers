class Point:

    default_color = "red"
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self):
        print(f"Point({self.x}, {self.y})")

    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def draw(self):
        print(f"Point({self.x}, {self.y})")

    def __eq__(self, value):
        return self.x == value.x and self.y == value.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    @classmethod
    #cls is passed as the first argument to class methods
    def zero(cls):
        return cls(0,0)
    
    def __iter__(self):
       return iter(self.__tags)


point = Point(1, 2)
print(str(point))
print(point.default_color)
print(Point.default_color)
point.draw()                 

another = Point(3, 4)
another.draw()
