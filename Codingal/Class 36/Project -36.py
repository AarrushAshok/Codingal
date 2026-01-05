#Custom Event
import pygame
import random

pygame.init()
WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))

CHANGE = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE, 1000)

class MySprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))  # start red
        self.rect = self.image.get_rect(topleft=(x, y))

    def change_color(self):
        # Random color
        self.image.fill((
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        ))

# Create sprites
sprite1 = MySprite(100, 120)
sprite2 = MySprite(250, 120)

# Sprite group
all_sprites = pygame.sprite.Group(sprite1, sprite2)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Custom event: change sprite colors
        if event.type == CHANGE:
            for sprite in all_sprites:
                sprite.change_color()

    # Draw
    screen.fill((30, 30, 30))  # background color
    all_sprites.draw(screen)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()