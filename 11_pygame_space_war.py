import pygame
import random
import math

pygame.init()

# Main Screen
screen = pygame.display.set_mode((600,957)) 

# load wallpaper 
wallpaper = pygame.image.load('background-wallpaper.jpg')

# Title and Icon
pygame.display.set_caption(".::SPACE WAR::.")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Player 
playerImg = pygame.image.load('player.png')
playerX = 268
playerY = 720
playerX_change = 0 

# enemy 
enemyType = random.randint(1,4)
if enemyType == 1 :
    enemyImg = pygame.image.load('enemy1.png')
elif enemyType == 2 :
    enemyImg = pygame.image.load('enemy2.png')
elif enemyType == 3 :
    enemyImg = pygame.image.load('enemy3.png')
elif enemyType == 4 :
    enemyImg = pygame.image.load('enemy4.png')

enemyX = random.randint(100,400)
enemyY = random.randint(50,150)
enemyX_change = 0.1 
enemyY_change = 10 

# bullet 
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 720
bulletX_change = 0.1 
bulletY_change = 1
bullet_state = "ready"
score = 0 

def fire_bullet(x,y):
    screen.blit(bulletImg,(x+10,y+20))

def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y):
    screen.blit(enemyImg ,(x,y))

def isCollision(x1,y1,x2,y2):
    # calculate distance between (x1,y1) and (x2,y2)
    distance = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
    if distance < 30 :
        return True
    else :
        return False

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
            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    bulletX = playerX
                    bullet_state = "fire"
                    fire_bullet(bulletX,bulletY)

        if event.type == pygame.KEYUP:
           if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
               playerX_change = 0


    screen.fill((0,128,128))
    screen.blit(wallpaper,(0,0))

    # player movement
    playerX += playerX_change
    if playerX <= 0:
         playerX = 0 
    elif playerX >=536 :
        playerX = 536

    # enemy movement
    enemyX += enemyX_change
    if enemyX <= 0:
         enemyX_change = 0.1
         enemyY += enemyY_change
    elif enemyX >=536 :
         enemyX_change = -0.1
         enemyY += enemyY_change

    # bullet movement 
    if bullet_state is 'fire':
        if bulletY <= 0 : 
            bullet_state = 'ready'
            bulletY = 720
        
        fire_bullet(bulletX , bulletY)
        bulletY -= bulletY_change
    # bullet collision 
    collision = isCollision(enemyX , enemyY , bulletX , bulletY )
    if collision:
        bullet_state = 'ready'
        bulletY = 720
        score += 1
        print(score)
        enemyX = random.randint(100,400)
        enemyY = random.randint(50,150)

    player(playerX,playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()
    
