import pygame
import random
import math

# Initializing pygame

pygame.init()

# Creating a screen

screen = pygame.display.set_mode((800, 600))

# Adding Title
pygame.display.set_caption("Space Bombers")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
background = pygame.image.load('background.png')
playerImg = pygame.image.load('player.png')

playerX = 370
playerY = 480

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_enemies = 6
for i in range(0, num_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(3)
    enemyY_change.append(0)

bulletImg = pygame.image.load('bullet.png')
en = pygame.image.load('enemy.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"


def player(x, y):
    screen.blit(playerImg, (x, y))


def iscollision(enemyX, enemyY, bulletX, bulletY):
    if math.sqrt(pow(enemyX - bulletX, 2) + pow(enemyY - bulletY, 2)) > 27:
        return False

    return True


score_value = 0
textX = 10
textY = 10
font = pygame.font.Font('freesansbold.ttf', 32)


def showScore(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def enemy(x, y):
    screen.blit(en, (x, y))


temp = 0


def fireBullet(x, y):
    global bullet_state
    global temp
    if bullet_state is "ready":
        temp = x
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


playerX_change = 0

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                fireBullet(playerX, playerY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerX_change = 0

    playerX += playerX_change

    # enemyY+=enemyY_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    for i in range(0, num_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX[i] = 0
            enemyX_change[i] = 3
            enemyY[i] += 40
        elif enemyX[i] >= 736:
            enemyX[i] = 736
            enemyX_change[i] = -3
            enemyY[i] += 40
        collision = iscollision(enemyX[i], enemyY[i], temp, bulletY)
        if collision:
            bullet_state = "ready"
            bulletY = 480
            score_value += 1
            print(score_value)
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i])
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fireBullet(temp, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    showScore(textX, textY)
    pygame.display.update()
