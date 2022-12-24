import math
import pygame
class Point_line:
    # constructed using a normal tupple
    def __init__(self, point_t = (0,0)):
        self.x = float(point_t[0])
        self.y = float(point_t[1])

    # define all useful operators
    def __add__(self, other):
        return Point_line((self.x + other.x, self.y + other.y))

    def __sub__(self, other):
        return Point_line((self.x - other.x, self.y - other.y))

    def __mul__(self, scalar):
        return Point_line((self.x*scalar, self.y*scalar))

    def __div__(self, scalar):
        return Point_line((self.x/scalar, self.y/scalar))

    def __len__(self):
        return int(math.sqrt(self.x**2 + self.y**2))

    # get back values in original tuple format
    def get(self):
        return (self.x, self.y)

#Drawing dashed line aroud selected shape
def draw_dashed_line(surf, color, start_pos, end_pos, width=1, dash_length=10):
    origin = Point_line(start_pos)
    target = Point_line(end_pos)
    displacement = target - origin
    length = len(displacement)
    slope = displacement/length

    for index in range(0, length/dash_length, 2):
        start = origin + (slope *    index    * dash_length)
        end   = origin + (slope * (index + 1) * dash_length)
        pygame.draw.line(surf, color, start.get(), end.get(), width)