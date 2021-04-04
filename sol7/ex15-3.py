import copy

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
    new_rect = copy.deepcopy(rect)
    new_rect.ld_corner.x += dx
    new_rect.ld_corner.y += dy
    return new_rect

rect = Rectangle()
rect.set_width_height(100, 100)
rect.set_ld_point(3, 4)

shifted_rect = move_rectangle(rect, 17, 16)

print(rect.ld_corner.x, rect.ld_corner.y)
print(shifted_rect.ld_corner.x, shifted_rect.ld_corner.y)