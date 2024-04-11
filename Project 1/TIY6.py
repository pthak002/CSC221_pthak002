import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple Space Shooter")

# Colors
PINK = (255, 192, 203)

# Set up the clock
clock = pygame.time.Clock()

# Load the player's ship image and resize it
ship_image = pygame.image.load("images/ship.png")
ship_image = pygame.transform.scale(ship_image, (70, 70))  # Resize to 40x40 pixels
ship_rect = ship_image.get_rect()
ship_y = screen_height // 2 - ship_rect.height // 2
ship_speed = 5

# Set up the bullet
bullet_width = 10
bullet_height = 5
bullet_speed = 7
bullets = []

# Game loop
while True:
    screen.fill(PINK)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(pygame.Rect(ship_rect.right, ship_y + ship_rect.height // 2 - bullet_height // 2, bullet_width, bullet_height))

    # Move the player's ship
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and ship_y > 0:
        ship_y -= ship_speed
    if keys[pygame.K_DOWN] and ship_y < screen_height - ship_rect.height:
        ship_y += ship_speed

    # Move the bullets
    for bullet in bullets:
        bullet.x += bullet_speed

    # Delete bullets that are off the screen
    bullets = [bullet for bullet in bullets if bullet.x < screen_width]

    # Draw the player's ship
    screen.blit(ship_image, (0, ship_y))

    # Draw the bullets
    for bullet in bullets:
        pygame.draw.rect(screen, (255, 255, 0), bullet)

    # Update the screen
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
