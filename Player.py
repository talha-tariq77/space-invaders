from Constants import *
import pygame


class Player:  # The Player Object
    def __init__(self):
        self.image = pygame.image.load('player_image.png')
        self.x = Player_start_x
        self.y = Player_start_y
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.pos = self.x, self.y
        self.damage = 10
        self.health_number = 100
        self.yspeed = 4
        self.xspeed = 4
        self.repeated_objects = []
        self.realy = self.y
        self.realx = self.x
        self.bullet_delay = 0.1 * FPS

    def move(self, x, y):
        self.x += x * self.xspeed
        self.y += y * self.yspeed
        if self.x >= Game_w - self.w:
            self.x = Game_w - self.w
        elif self.x <= 0:
            self.x = 0
        if self.y >= Game_h - self.h:
            self.y = Game_h - self.h
        elif self.y <= 0:
            self.y = 0

    def render(self, window):
        if self.health_number <= 0:
            Game_switches['GamePhase3'] = 'Lost'
            self.health_number = 1
            Game_switches['GamePhase2'] = False
        health_bar = pygame.Surface((self.health_number, 10))
        health_bar.fill(Green)
        window.blit(self.image, (self.x, self.y))
        window.blit(health_bar, (self.x + self.w / 2 - self.health_number / 2, self.y + self.h))

    def stat_increase(self):
        self.damage += 1
        self.xspeed += 0.1
        self.yspeed += 0.1
        self.health_number += 1
