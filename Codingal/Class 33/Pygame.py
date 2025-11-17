#Pygame
import pygame
width = 500
height = 500
pygame.display.set_mode((width, height))

gameRunningStatus = True
while gameRunningStatus:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunningStatus = False