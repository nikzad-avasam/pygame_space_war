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

def player(x,y):
    screen.blit(playerImg,(x,y))

# Game Frames 
running = True
while running:
    playerX += 0.05
    print(playerX)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,128,128))
    player(playerX,playerY)
    pygame.display.update()
    
