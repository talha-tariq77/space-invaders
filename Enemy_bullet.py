from Constants import *
import pygame
import math


def compare(x, y):
    if x > y:
        return True
    elif x < y:
        return False
    else:
        return 'same'

def HCF(x, y):
    templist = []
    for i in range(1, 100):
        if x % i == 0 and y % i == 0:
            templist.append(i)
    return templist[-1]


class EnemyBullet:
    def __init__(self, x, y, type, playerx, playery):
        self.image = pygame.image.load(bullet_images[type])
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.x = x
        self.y = y
        self.type = type
        self.speed = bullet_speed[self.type]
        self.damage_number = bullet_damage[self.type]
        self.playerx = playerx
        self.playery = playery
        self.decay = 7 * FPS
        if self.type == 2 or self.type == 3:
            self.xadd, self.yadd = self.type2check(self.playerx, self.playery)

    def render(self, window):
        window.blit(self.image, (self.x, self.y))

    def move(self):
            self.y += self.speed

    def type2check(self, playerx, playery):
        # assumes top right part of graph
        xdiff = playerx - self.x
        ydiff = playery - self.y
        xadd = 0
        yadd = 0
        simply = ydiff
        simplx = xdiff
        if xdiff > ydiff and xdiff != 0 != ydiff:
            if simply < 0:
                simply *= -1
            xadd = xdiff / simply
            yadd = ydiff / simply
        elif xdiff < ydiff and xdiff != 0 != ydiff:
            if simplx < 0:
                simplx *= -1
            xadd = xdiff / simplx
            yadd = ydiff / simplx
        else:
            xadd = 1
            yadd = 1
        return xadd, yadd

    def type2move(self):
        self.x += self.xadd
        self.y += self.yadd
