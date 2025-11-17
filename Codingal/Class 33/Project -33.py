#Football
import pygame
pygame.init()

width = 500
height = 500
screen = pygame.display.set_mode((width, height))
bgimage = pygame.image.load(r"Class 33/Pygame_BG.jpeg")
bgimage = pygame.transform.scale(bgimage, (width, height))

gameRunningStatus = True
ballX = width // 2  # Init X of the ball
ballY = height // 2  # Init Y of the ball
ball_radius = 30
ballX_speed = 1
ballY_speed = 1

while gameRunningStatus:
    screen.fill("violet")
    screen.blit(bgimage, (0, 0))
    pygame.draw.circle(screen, "RED", (ballX, ballY), ball_radius)
    ballX += ballX_speed
    ballY += ballY_speed

    if ballX - ball_radius <= 0 or ballX + ball_radius >= width:
        ballX_speed = -ballX_speed
    if ballY - ball_radius <= 0 or ballY + ball_radius >= height:
        ballY_speed = -ballY_speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunningStatus = False
    
    pygame.display.update()