import sys
import pygame 

#Initialisation de pygame
pygame.init()

#Creation d'un fenetre nommé "Ninja Game" de dimensions/resolution 640x480
pygame.display.set_caption('Ninja Game')
screen = pygame.display.set_mode((640, 480))

#Initialisation d'une montre pour faire tourné le jeu en 60fps
clock = pygame.time.Clock()

#Creation de la game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            sys.exit()
    
    pygame.display.update()
    clock.tick(60)