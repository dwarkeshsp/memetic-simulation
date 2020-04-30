import math


class Society:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, x, y):
        return math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
