# imports
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


class GameObj(pygame.sprite.Sprite):

    family = pygame.sprite.RenderUpdates()

    def __init__(self):
        super().__init__()
        self.family.add(self)


class Ball(GameObj):
    radius = 20

    family = pygame.sprite.GroupSingle()

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((2 * self.radius, 2 * self.radius))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.family.add()


def game():
    while True:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q] and (keys[pygame.K_LMETA] or keys[pygame.K_RMETA]) or pygame.event.peek(pygame.QUIT):  # Quit
            pygame.quit()
            sys.exit()
        GameObj.family.draw(display)
        pygame.display.update()


game()
