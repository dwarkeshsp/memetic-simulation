import pygame
import random
import matplotlib.pyplot as plt
from person import Person
from meme import Meme
from society import Society

SCREEN_SIZE = 1000

clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Memetic Evolution Simulation')
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE), 0, 32)


missionary = Meme(spread=100, color=(51, 153, 255))
cult = Meme(spread=5, color=(0, 204, 0))

society_1 = Society(SCREEN_SIZE / 3, SCREEN_SIZE / 2)
society_2 = Society(2 * SCREEN_SIZE/3, SCREEN_SIZE/2)


people = []
for _ in range(100):
    people.append(Person(society=society_1))
people.append(Person(society=society_1, meme=missionary))

for _ in range(100):
    people.append(Person(society=society_2))
people.append(Person(society=society_2, meme=cult))


running = True

while running:

    screen.fill((0, 0, 0))

    for person in people:
        person.move()

        if person.meme:
            for other_person in people:
                if person.rect.colliderect(other_person.rect):
                    # 5 percent change
                    if 5 > random.randint(0, 100):
                        other_person.meme = person.meme

        pygame.draw.rect(screen, person.color(), person.rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(50)
