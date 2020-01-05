import pygame
import random

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

enemyImg = pygame.image.load('enemy.png')

enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 3
enemyY_change = 0

bulletImg = pygame.image.load('bullet.png')

bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fireBullet(x, y):
    global bullet_state
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
    enemyX += enemyX_change
    # enemyY+=enemyY_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    if enemyX <= 0:
        enemyX = 0
        enemyX_change = 3
        enemyY += 40
    elif enemyX >= 736:
        enemyX = 736
        enemyX_change = -3
        enemyY += 40

    if bullet_state is "fire":
        fireBullet(playerX,bulletY)
        bulletY-=bulletY_change
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
