import pygame

#Initializing pygame

pygame.init()

#Creating a screen

screen = pygame.display.set_mode((800 , 600))

#Adding Title
pygame.display.set_caption("Space Bombers")
icon =pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

playerImg =pygame.image.load('player.png')

playerX = 370
playerY = 480

def  player():
    screen.blit(playerImg,(playerX,playerY))


running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()
    pygame.display.update()





