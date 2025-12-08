#Ball Game
import pygame
pygame.init()

width = 500
height = 500
screen = pygame.display.set_mode((width, height))

bgimage = pygame.image.load(r"/Users/Aarrush/Documents/Aarush/Coding/Codingal/Class 33/Pygame_BG.jpeg")
bgimage = pygame.transform.scale(bgimage, (width, height))
clock = pygame.time.Clock()

ballx = width // 2
bally = height // 2
ball_radius = 30
ballx_speed = 1
bally_speed = 1

class Ball(pygame.sprite.Sprite):
    def __init__(self, ballx, bally, ball_radius):
        super().__init__()
        self.image = pygame.Surface((2 * ball_radius, 2 * ball_radius), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 0, 0), (ball_radius, ball_radius), ball_radius)
        self.rect = self.image.get_rect(center=(ballx, bally))

ball = Ball(ballx, bally, ball_radius)
ball_group = pygame.sprite.Group()
ball_group.add(ball)

gameRunningStatus = True
while gameRunningStatus:
    clock.tick(60)
    screen.fill((238, 130, 238))  # Fill screen with violet color (RGB for violet: (238, 130, 238))
    screen.blit(bgimage, (0, 0))  # Draw the background image
    ball_group.draw(screen)  # Draw the ball sprite

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunningStatus = False

    ball.rect.x += ballx_speed
    ball.rect.y += bally_speed

    if ball.rect.left <= 0 or ball.rect.right >= width:
        ballx_speed = -ballx_speed
    if ball.rect.top <= 0 or ball.rect.bottom >= height:
        bally_speed = -bally_speed

    pygame.display.update()
    
pygame.quit()