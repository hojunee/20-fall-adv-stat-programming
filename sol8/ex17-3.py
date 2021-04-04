class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return ("점 ({}, {})".format(self.x, self.y))
        
a = Point(3, 4)
print(a)

b = Point(8, 2)
print(b)