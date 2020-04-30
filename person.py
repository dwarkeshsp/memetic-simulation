import random
import pygame


class Person:
    def __init__(self, root_x, root_y, meme):

        self.root_x = root_x
        self.root_y = root_y
        self.meme = meme
        self.dx = 0
        self.dy = 0

        def random_location(root):
            return random.randint(0, 100) - 50 + root

        self.rect = pygame.Rect(0, 0, 5, 5)
        self.rect.center = (random_location(root_x),
                            random_location(root_y))

    def move(self):

        self.rect.x += self.dx
        self.rect.y += self.dy

        def random_speed():
            return random.randint(0, 20) / 10 - 1

        def gravity(root, n):
            gravity = (root - n) ** 2 / (self.meme.spread * 1000)
            if n > root:
                gravity *= -1
            return gravity

        self.dx += random_speed() + gravity(self.root_x,  self.rect.x)
        self.dy += random_speed() + gravity(self.root_y, self.rect.y)

        DECELERATION = 0.99
        self.dx *= DECELERATION
        self.dy *= DECELERATION

    def color(self):
        return self.meme.color
