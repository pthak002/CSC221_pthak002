import pygame
import sys
import random

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Alien Invasion")


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

clock = pygame.time.Clock()

ship_image = pygame.image.load("ship.png")
ship_image = pygame.transform.scale(ship_image, (70, 70)) 
ship_rect = ship_image.get_rect()
ship_y = screen_height // 2 - ship_rect.height // 2
ship_speed = 5

alien_image = pygame.image.load("alien.png")
alien_image = pygame.transform.scale(alien_image, (50, 50)) 
alien_rect = alien_image.get_rect()
alien_speed = 3


bullet_width = 10
bullet_height = 5
bullet_speed = 7
bullets = []


aliens = []


while True:
    screen.fill(BLACK)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(pygame.Rect(ship_rect.right, ship_y + ship_rect.height // 2 - bullet_height // 2, bullet_width, bullet_height))

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and ship_y > 0:
        ship_y -= ship_speed
    if keys[pygame.K_DOWN] and ship_y < screen_height - ship_rect.height:
        ship_y += ship_speed

  
    for bullet in bullets:
        bullet.x += bullet_speed

   
    bullets = [bullet for bullet in bullets if bullet.x < screen_width]

   
    for alien in aliens:
        alien.x -= alien_speed


    if random.randint(1, 100) == 1:
        new_alien_y = random.randint(0, screen_height - alien_rect.height)
        new_alien = alien_rect.copy()
        new_alien.x = screen_width
        new_alien.y = new_alien_y
        aliens.append(new_alien)

  
    aliens = [alien for alien in aliens if alien.x > 0]

    for bullet in bullets[:]:
        for alien in aliens[:]:
            if bullet.colliderect(alien):
                aliens.remove(alien)
                bullets.remove(bullet)

  
    for alien in aliens:
        if alien.colliderect(ship_rect):
            pygame.quit()
            sys.exit()
  
    screen.blit(ship_image, (0, ship_y))

    for alien in aliens:
        screen.blit(alien_image, (alien.x, alien.y))
  
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, bullet)
    
    pygame.display.flip()

    clock.tick(60)
