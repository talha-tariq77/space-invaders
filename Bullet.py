from Constants import *
import pygame


class Bullet:
    def __init__(self, x, y, damage):
        self.image = pygame.image.load('bullet.png')
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.x = x
        self.y = y
        self.speed = 6
        self.damage_number = damage

    def render(self, window):
        window.blit(self.image, (self.x, self.y))

    def move(self):
        self.y -= 1 * self.speed

