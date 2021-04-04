class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return ("점 ({}, {})".format(self.x, self.y))
        
    def __add__(self, other):
        return (self.x + other.x, self.y + other.y)

a = Point(3, 4)
b = Point(8, 2)
print(a + b)