import math


class Society:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, person):
        return math.sqrt((self.x - person.rect.x) ** 2 + (self.y - person.rect.y) ** 2)
