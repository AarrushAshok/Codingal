#Dino Game
import pygame, random, time


pygame.init()

h = 500
w = 500
screen = pygame.display.set_mode((h,w))
img = pygame.image.load("Class 37/Flappy Bird BG.png")
img = pygame.transform.scale(img,(h,w))
dino = pygame.transform.scale(pygame.image.load("Class 38/Dino.png"),(100,200))
playerX = h//2
playerY = w//2
posX = random.randint(50,450)
posY = random.randint(50,450)

player = pygame.Rect(playerX,playerY,100,50)
enemy = pygame.Rect(posX,posY,50,50)

gameObj = pygame.Surface((100,200),pygame.SRCALPHA)
# enemy = pygame.Surface((50,50),pygame.SRCALPHA)
speed = random.randint(4,8) #speedx
speedY = random.randint(4,8)

setUpperLimit = h-200-200
normalPos = h -200
runningStatus = True
while runningStatus:
    pygame.time.Clock().tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runningStatus = False
        if event.type == pygame.MOUSEBUTTONUP:
            posX,posY = pygame.mouse.get_pos()
            # enemy = pygame.Surface((50,50),pygame.SRCALPHA)
            enemy = pygame.Rect(posX,posY,50,50)
            print(posX,posY)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and playerX>0:
                playerX -=15
            if event.key == pygame.K_RIGHT and playerX < w-100:
                playerX +=15
            if event.key == pygame.K_UP:
                normalPos = setUpperLimit
                playerY -=15
            if event.key == pygame.K_DOWN:
                playerY +=15
                # player.y +=15
    if normalPos < h-200:       
     normalPos += 5
    # screen.fill("RED")
    screen.blit(img,(0,0))
    pygame.draw.rect(screen,"green",(playerX,playerY,100,50))
    gameObj.blit(dino,(0,0))
    screen.blit(gameObj,(100,normalPos))


    # pygame.draw.circle(enemy,"red",(25,25),20)
    
    pygame.draw.rect(screen,"red",enemy)
    enemy.x += speed
    enemy.y += speedY
    if enemy.x > w-50 or enemy.x < 0:
        speed = -speed #speedx
    if enemy.y > h-50  or enemy.y <0 :
        speedY = -speedY
        
       
    # time.sleep(1)
    # screen.blit(enemy,(posX,posY))
    if player.colliderect(enemy):
          screen.fill(random.choice(["red","green","blue","purple","yellow"]))
    
    pygame.display.flip()