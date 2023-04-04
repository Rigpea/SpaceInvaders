import pygame

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Rigpooooooooo")
icon = pygame.image.load('rigpooooooo.png')
pygame.display.set_icon(icon)
playerImg = pygame.image.load('poopoo.png')

playerX = 100
playerY = 100

def player(x,y):
    screen.blit(playerImg, (x, y))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX += 1
            if event.key == pygame.K_LEFT:
                playerX -= 1
            if event.key == pygame.K_UP:
                playerY -= 1
            if event.key == pygame.K_DOWN:
                playerY += 1


    screen.fill((255, 255, 255))
    player(playerX,playerY)
    pygame.display.update()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
