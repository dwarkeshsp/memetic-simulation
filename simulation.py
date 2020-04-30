import pygame
import random
import matplotlib.pyplot as plt
from person import Person
from meme import Meme
from society import Society

SCREEN_SIZE = 1000


dynamism = Meme(spread=100, color=(255, 255, 255))
society_1 = Society(x=SCREEN_SIZE/2, y=SCREEN_SIZE/2)

people = []
for _ in range(1):
    people.append(Person(society=society_1, meme=dynamism))

clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Memetic Evolution Simulation')
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE), 0, 32)

running = True

while running:

    screen.fill((0, 0, 0))

    for person in people:
        person.move()
        pygame.draw.rect(screen, person.color(), person.rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(50)
