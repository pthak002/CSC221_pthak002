import pygame

class CharacterDrawer:
    def __init__(self, character_image_path, background_color):
        pygame.init()
        self.window_width, self.window_height = 800, 600
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Character Drawer")

        self.character_image = pygame.image.load(character_image_path)
        self.character_image = self.match_background_color(self.character_image, background_color)
        self.character_image = pygame.transform.scale(self.character_image, (100, 100))  # Resize the image

        self.background_color = background_color
        self.running = True

    def match_background_color(self, image, color):
        image = image.convert()
        image.set_colorkey((0, 0, 0))
        image = image.convert_alpha()

        rect = image.get_rect()
        temp = pygame.Surface(rect.size, pygame.SRCALPHA, 32)
        temp.blit(image, (0, 0))
        temp.fill(color + (0,), None, pygame.BLEND_RGBA_MAX)
        temp.blit(image, (0, 0), None, pygame.BLEND_RGB_MAX)

        return temp

    def draw_character(self):
        while self.running:
            self.screen.fill(self.background_color)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            character_rect = self.character_image.get_rect()
            character_rect.midbottom = (self.window_width // 2, self.window_height)  # Position at bottom center
            self.screen.blit(self.character_image, character_rect)

            pygame.display.flip()

        pygame.quit()

# Example usage
character_drawer = CharacterDrawer("images/character.png", (0, 0, 255))  # Blue background
character_drawer.draw_character()