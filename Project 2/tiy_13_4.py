import random
import pygame
from pygame.locals import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
DROP_SIZE = 30  
DROP_COLOR = (0, 0, 255)
NUM_ROWS = 5  
RAINDROPS_PER_ROW = 10 
FALL_SPEED = 4 

class Raindrop:
    def __init__(self, image, x, y):
        self.image = pygame.transform.scale(image, (DROP_SIZE, DROP_SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def fall(self):
        self.rect.y += FALL_SPEED

        if self.rect.y > SCREEN_HEIGHT:
            self.rect.y = random.randint(-DROP_SIZE * 2, -DROP_SIZE)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Rain")
    clock = pygame.time.Clock()

    raindrop_image = pygame.image.load('raindrop.png').convert_alpha()

    raindrops = []

    
    for row in range(NUM_ROWS):
        y = -row * (DROP_SIZE * 2) 
        for i in range(RAINDROPS_PER_ROW):
            x = (SCREEN_WIDTH // (RAINDROPS_PER_ROW + 1)) * (i + 1) - (DROP_SIZE // 2)
            raindrops.append(Raindrop(raindrop_image, x, y))

    running = True
    current_row = 0  
    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        if current_row < NUM_ROWS:
            for i in range(RAINDROPS_PER_ROW):
                raindrops[current_row * RAINDROPS_PER_ROW + i].fall()

            
            if raindrops[current_row * RAINDROPS_PER_ROW].rect.y >= SCREEN_HEIGHT:
                current_row += 1  

        
        for drop in raindrops:
            drop.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
