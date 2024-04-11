import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rocket Game")

# Load the rocket image
rocket_image = pygame.image.load("images/rocket.png")
rocket_image = pygame.transform.scale(rocket_image, (50, 100))  # Resize the image
rocket_rect = rocket_image.get_rect()
rocket_rect.center = (screen_width // 2, screen_height // 2)

# Set up the game loop
running = True
clock = pygame.time.Clock()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rocket_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        rocket_rect.x += 5
    if keys[pygame.K_UP]:
        rocket_rect.y -= 5
    if keys[pygame.K_DOWN]:
        rocket_rect.y += 5

    # Keep the rocket within the screen boundaries
    rocket_rect.clamp_ip(screen.get_rect())

    # Clear the screen
    screen.fill((0, 0, 255))  # Blue color

    # Draw the rocket
    screen.blit(rocket_image, rocket_rect)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()