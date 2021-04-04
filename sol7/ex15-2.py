class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle():
    def set_width_height(self, w, h):
        self.width = w
        self.height = h

    def set_ld_point(self, x, y):
        self.ld_corner = Point(x, y)

def move_rectangle(rect, dx, dy):
    rect.ld_corner.x += dx
    rect.ld_corner.y += dy

rect = Rectangle()
rect.set_width_height(100, 100)
rect.set_ld_point(3, 4)

move_rectangle(rect, 17, 16)

print(rect.ld_corner.x, rect.ld_corner.y)