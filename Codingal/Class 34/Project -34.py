#Ball and Bat Game with Score
import pygame
pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Ball
ballX, ballY = 50, 50
ball_speedX, ball_speedY = 5, 3

# Bat
bat_width, bat_height = 120, 20
batX = width // 2 - bat_width // 2
batY = height - 50
bat_speed = 20

# Score
score = 0
font = pygame.font.Font(None, 40)

runningStatus = True
while runningStatus:
    clock.tick(60)
    screen.fill("GREEN")

    pygame.draw.circle(screen, "RED", (ballX, ballY), 30)
    ballX += ball_speedX
    ballY += ball_speedY

    if ballX <= 30 or ballX >= width - 30:
        ball_speedX = -1
    if ballY <= 30:
        ball_speedY = -1

    if batY - 30 <= ballY <= batY and batX <= ballX <= batX + bat_width:
        ball_speedY = -1
        score += 1  # Increase score

    pygame.draw.rect(screen, "BLUE", (batX, batY, bat_width, bat_height))
    score_text = font.render(f"Score: {score}", True, "WHITE")
    screen.blit(score_text, (10, 10))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runningStatus = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                batX -= bat_speed
            if event.key == pygame.K_RIGHT:
                batX += bat_speed