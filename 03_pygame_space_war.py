import pygame

pygame.init()

# Main Screen
screen = pygame.display.set_mode((500,600))

# Title and Icon
pygame.display.set_caption(".::SPACE WAR::.")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Player 
playerImg = pygame.image.load('player.png')
playerX = 225
playerY = 450

def player():
    screen.blit(playerImg,(playerX,playerY))

# Game Frames 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((181,128,128))
    player()
    pygame.display.update()
    
