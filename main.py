# initialisation

# Imports
import pygame
import sys
import os

pygame.init()

# colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIDTH = 800
HEIGHT = 800
display = pygame.display.set_mode((WIDTH, HEIGHT))

def game():
    while True:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q] and (keys[pygame.K_LMETA] or keys[pygame.K_RMETA]) or pygame.event.peek(pygame.QUIT):  # Quit
            pygame.quit()
            sys.exit()
        GameObj.family.draw(display)
        pygame.display.update()

game()
