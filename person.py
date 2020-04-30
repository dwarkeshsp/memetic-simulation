import random
import pygame


class Person:
    def __init__(self, society, meme=None):

        self.society = society
        self.meme = meme
        self.dx = 0
        self.dy = 0

        def random_location(root):
            return random.randint(0, 100) - 50 + root

        self.rect = pygame.Rect(0, 0, 5, 5)
        self.rect.center = (random_location(society.x),
                            random_location(society.y))

    def move(self):

        self.rect.x += self.dx
        self.rect.y += self.dy

        def random_speed():
            return random.randint(0, 20) / 10 - 1

        def gravity(root, n):
            gravity = (root - n) ** 2 / (self.spread() * 1000)
            if n > root:
                gravity *= -1
            return gravity

        self.dx += random_speed() + gravity(self.society.x,  self.rect.x)
        self.dy += random_speed() + gravity(self.society.y, self.rect.y)

        DECELERATION = 0.99
        self.dx *= DECELERATION
        self.dy *= DECELERATION

    def spread(self):
        return self.meme.spread if self.meme else 50

    def color(self):
        return self.meme.color() if self.meme else (255, 255, 255)
