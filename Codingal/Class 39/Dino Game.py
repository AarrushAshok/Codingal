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
        super().__init__()
        self.image = pygame.image.load("Class 38/Dino.png")
        self.image = pygame.transform.scale(self.image,(50,100))
        self.rect = self.image.get_rect(center=(100,h-50))

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.K_SPACE:
                newY = self.rect.y -100
                self.rect = self.image.get_rect(self.rect.x,newY)
dino = Dino()

sprite_group = pygame.sprite.Group()
sprite_group.add(dino)

runningStatus = True
while runningStatus:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runningStatus = False

screen.blit(bgimg,(0,0))
sprite_group.draw(screen)
sprite_group.update()
pygame.display.update()