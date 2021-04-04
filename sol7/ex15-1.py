import math

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
a = Point(3, 4)
b = Point(6, 8)

def distance_between_points(point_a, point_b):
    return math.sqrt((point_a.x - point_b.x)**2 + (point_a.y - point_b.y)**2)

print(distance_between_points(a, b))