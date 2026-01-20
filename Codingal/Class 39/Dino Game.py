#Dino Game
import pygame
pygame.init()

h,w = 500,500
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption("Dino Game")

img = pygame.image.load("Class 37/Flappy Bird BG.png")
bgimg = pygame.transform.scale(img,(w,h))

#Game Object Class
class Dino(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("Class 38/Dino.png")
        self.image = pygame.transform.sclae(self.image,(50,100))
        self.rect = self.image.get_rect(center=(w//2,h//2))
    def update(self):
        pass

runningStatus = True
while runningStatus:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runningStatus = False

screen.blit(bgimg,(0,0))
pygame.display.update()