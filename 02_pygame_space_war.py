import pygame

pygame.init()

# Main Screen
screen = pygame.display.set_mode((800,400))
# Title and Icon
pygame.display.set_caption(".::SPACE WAR::.")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Game Frames 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((181,128,128))
    pygame.display.update()
    
