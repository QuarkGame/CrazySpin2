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

# screen
WIDTH = 1200
HEIGHT = 600
display = pygame.display.set_mode((WIDTH, HEIGHT))


# name the window
pygame.display.set_caption("Crazy Spin 2")

class GameObj(pygame.sprite.Sprite):

    family = pygame.sprite.RenderUpdates()

    def __init__(self):
        super().__init__()
        GameObj.family.add(self) # EDWARD!!!! YOU CAN NOT USE self.family.add(self) !!!!!!!!!!!!!!!!!!!!!!!!


class Ball(GameObj):
    radius = 10

    family = pygame.sprite.GroupSingle() # pygame.sprite.GroupSingle()

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((2 * self.radius, 2 * self.radius))
        pygame.draw.circle(self.image, RED, (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        Ball.family.add(self)
        self.x = 3
        self.y = 3

    def update(self):
        if self.rect.y - self.radius * 2 < 0 or self.rect.y + self.radius * 2 > HEIGHT:
            self.y = -self.y
        if pygame.sprite.collide_rect(self, PlayerPad.family.sprite) or pygame.sprite.collide_rect(self, EnemyPad.family.sprite):
            self.x = -self.x
        self.rect.x += self.x
        self.rect.y += self.y


class PlayerPad(GameObj):

    height = 100
    width = 20

    family = pygame.sprite.GroupSingle()

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (self.width / 2, HEIGHT / 2)
        PlayerPad.family.add(self)

    def move(self, y):
        self.rect.y += y
        if self.rect.y <= 0:
            self.rect.y = 0
        if self.rect.y + PlayerPad.height >= HEIGHT:
            self.rect.y = HEIGHT - PlayerPad.height


    def update(self):
        pass


class EnemyPad(GameObj):

    height = 100
    width = 20

    family = pygame.sprite.GroupSingle()

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH - self.width / 2, HEIGHT / 2)
        EnemyPad.family.add(self)

    def move(self, y):
        self.rect.y += y
        if self.rect.y <= 0:
            self.rect.y = 0
        if self.rect.y + self.height >= HEIGHT:
            self.rect.y = HEIGHT - self.height


    def update(self):
        self.ai()


    def ai(self):
        if Ball.family.sprite.rect.y > self.rect.y:
            self.move(3)
        elif Ball.family.sprite.rect.y < self.rect.y:
            self.move(-3)
        else:
            pass


def game():
    Ball()
    PlayerPad()
    EnemyPad()
    while True:
        display.fill(BLACK)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q] and (keys[pygame.K_LMETA] or keys[pygame.K_RMETA]) or pygame.event.peek(pygame.QUIT):  # Quit
            pygame.quit()
            sys.exit()
        if keys[pygame.K_w]:
            PlayerPad.family.sprite.move(-3)
        if keys[pygame.K_s]:
            PlayerPad.family.sprite.move(3)

        GameObj.family.draw(display)
        GameObj.family.update()

        pygame.display.update()


game()
