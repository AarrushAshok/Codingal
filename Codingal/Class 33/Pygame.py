#Pygame
import pygame
pygame.init()

width = 500
height = 500
screen = pygame.display.set_mode((width, height))
bgimage = pygame.image.load(r"Class 33/Pygame_BG.jpeg")
bgimage = pygame.transform.scale(bgimage,(width,height))

gameRunningStatus = True

ballX = height//2
ballY = width//2
while gameRunningStatus:
    screen.fill("violet")
    screen.blit(bgimage,(0,0))
    pygame.draw.circle(screen,"RED",(ballX,ballY),30)
    pygame.draw.rect(screen,"YELLOW",(100,40,100,50))
    if 0 < ballX < width:
        ballX +=1
        ballY +=1
    else:
        ballX -= 1
        ballY -= 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunningStatus = False
    
    pygame.display.update()