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
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

WIDTH = 800
HEIGHT = 800
display = pygame.display.set_mode((WIDTH, HEIGHT))


class GameObj(pygame.sprite.Sprite):

    family = pygame.sprite.RenderUpdates()

    def __init__(self):
        super().__init__()
        GameObj.family.add(self) # EDWARD!!!! YOU CAN NOT USE self.family.add(self) !!!!!!!!!!!!!!!!!!!!!!!!


class Ball(GameObj):
    radius = 20

    family = pygame.sprite.RenderUpdates() # pygame.sprite.GroupSingle()

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((2 * self.radius, 2 * self.radius))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.family.add(self)


# class Block(GameObj):
#
#     # collision_detection
#     family = pygame.sprite.Group()
#
#     # Constructor. Pass in the color of the block,
#     # and its x and y position
#     def __init__(self, color, width, height):
#         super().__init__()
#
#         # Create an image of the block, and fill it with a color.
#         # This could also be an image loaded from the disk.
#         self.image = pygame.Surface([width, height])
#         self.image.fill(color)
#
#         # Fetch the rectangle object that has the dimensions of the image
#         # Update the position of this object by setting the values of rect.x and rect.y
#         self.rect = self.image.get_rect()
#         Block.family.add(self)


def game():
    Ball()
    # Block(GREEN, 100, 100)
    while True:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q] and (keys[pygame.K_LMETA] or keys[pygame.K_RMETA]) or pygame.event.peek(pygame.QUIT):  # Quit
            pygame.quit()
            sys.exit()

        GameObj.family.draw(display)

        pygame.display.update()


game()
