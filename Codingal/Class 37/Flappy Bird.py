# Flappy Bird
import pygame
import random

pygame.init()

WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))

bg_img = pygame.image.load("Class 37/Flappy Bird BG.png")
bg_img = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))

playerx = WIDTH // 2
playery = HEIGHT // 2
player = pygame.Rect(playerx, playery, 100, 50)

posx = random.randint(50, 450)
posY = random.randint(50, 450)
enemy = pygame.Rect(posx, posY, 50, 50)

runningStatus = True
clock = pygame.time.Clock()

while runningStatus:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runningStatus = False

        if event.type == pygame.MOUSEBUTTONUP:
            posx, posY = pygame.mouse.get_pos()
            enemy = pygame.Rect(posx, posY, 50, 50)
            print(posx, posY)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and playerx > 0:
                playerx -= 15
            if event.key == pygame.K_RIGHT and playerx < WIDTH - 100:
                playerx += 15
            if event.key == pygame.K_UP and playery > 0:
                playery -= 15
            if event.key == pygame.K_DOWN and playery < HEIGHT - 50:
                playery += 15

    player.x = playerx
    player.y = playery

    screen.blit(bg_img, (0, 0))
    pygame.draw.rect(screen, "green", player)
    pygame.draw.rect(screen, "red", enemy)

    if player.colliderect(enemy):
        screen.fill(random.choice(["red", "green", "blue", "purple", "yellow"]))

    pygame.display.flip()

pygame.quit()