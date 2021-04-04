class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return ("점 ({}, {})".format(self.x, self.y))
        
    def __add__(self, other):
        if isinstance(other, Point):
            return self.point_add(other)
        elif isinstance(other, tuple):
            return self.tuple_add(other)

    def point_add(self, other):
        return (self.x + other.x, self.y + other.y)

    def tuple_add(self, other):
        return (self.x + other[0], self.y + other[1])
        

a = Point(3, 4)
b = Point(8, 2)
print(a + b)
print(a + (8, 2))