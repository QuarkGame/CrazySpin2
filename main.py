# imports
import pygame
import sys
import os

pygame.init()

# colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255); GREY = (128, 128, 128)
RED = (255, 0, 0); DARK_READ = (128, 0, 0)
GREEN = (0, 255, 0); DARK_GREEN = (0, 128, 0)
BLUE = (0, 0, 255); DARK_BLUE = (0, 0, 128)
CYAN = (0, 255, 255); DARK_CYAN = (0, 128, 128)
MAGENTA = (255, 0, 255); DARK_MAGENTA = (128, 0, 128)
YELLOW = (255, 255, 0); DARK_YELLOW = (128, 128, 0)

WIDTH = 800
HEIGHT = 800
display = pygame.display.set_mode((WIDTH, HEIGHT))


class GameObj(pygame.sprite.Sprite):

    family = pygame.sprite.RenderUpdates()

    def __init__(self):
        super().__init__()
        GameObj.family.add(self) # EDWARD!!!! YOU CAN NOT USE self.family.add(self) !!!!!!!!!!!!!!!!!!!!!!!!


class Ball(GameObj):
    radius = 10

    family = pygame.sprite.RenderUpdates() # pygame.sprite.GroupSingle()

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((2 * self.radius, 2 * self.radius))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.family.add(self)


class Pad(GameObj):

    height = 10
    width = 100

    family = pygame.sprite.RenderUpdates()

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((self.height, self.width))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.family.add(self)

def game():
    Ball()
    Pad()
    while True:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q] and (keys[pygame.K_LMETA] or keys[pygame.K_RMETA]) or pygame.event.peek(pygame.QUIT):  # Quit
            pygame.quit()
            sys.exit()

        GameObj.family.draw(display)

        pygame.display.update()


game()
