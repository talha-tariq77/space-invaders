from Constants import *
import pygame


class Boss:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load('illuminati.png')
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.health_number = 1000
        self.counter = 0.1 * FPS
        self.reload = 0.1

    def render(self, window):
        window.blit(self.image, (self.x, self.y))

    def dec_health(self, dec):
        self.health_number += dec
