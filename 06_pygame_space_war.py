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
playerX_change = 0 

def player(x,y):
    screen.blit(playerImg,(x,y))

# Game Frames 
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.2
            if event.key == pygame.K_LEFT:
                playerX_change = -0.2
        if event.type == pygame.KEYUP:
           if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
               playerX_change = 0


    screen.fill((0,128,128))
    playerX += playerX_change
    if playerX <= 0:
         playerX = 0 
    elif playerX >=436 :
        playerX = 436


    player(playerX,playerY)
    pygame.display.update()
    
