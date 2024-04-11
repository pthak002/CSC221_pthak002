import sys

import pygame

pygame.init()

WIDTH, HEIGHT = 1200, 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Blue Background")

color = (0, 0, 255)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(color)
    pygame.display.flip()