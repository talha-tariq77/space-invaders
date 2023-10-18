from Constants import *
import pygame
import random


class Drop:
    def __init__(self, x, y, player, type):
        self.type = type - 1
        drop_images = ['drop.png', 'hpdrop.png']
        self.image = pygame.image.load(drop_images[self.type])
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.x = x
        self.y = y
        self.ymove = 1.5
        self.player = player

    def collisions(self, player):
        if self not in player.repeated_objects:
            if Detect_Collisions(self.x, self.y, self.x + self.w, self.y + self.h,
                                 player.x, player.y, player.x + player.w, player.y + player.h):
                if self.type == 0:
                    player.damage += 10
                elif self.type == 1:
                    player.health_number += 10
                player.repeated_objects.append(self)
                object_list.remove(self)

    def render(self, window):
        window.blit(self.image, (self.x, self.y))

    def delete(self):
        if self.y >= Game_h + self.h:
            object_list.remove(self)
            if self in self.player.repeated_objects:
                self.player.repeated_objects.remove(self)


class Enemy:  # Enemy object with different integrated types
    def __init__(self, x, y, enemy_type):
        self.y = int(y)
        self.x = int(x)
        self.type = enemy_type - 1
        self.image = pygame.image.load(enemy_images[self.type])
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.health_number = enemy_health[self.type]
        self.damage = enemy_damage[self.type]
        self.speed = 6
        self.right = True
        self.counter = enemy_reload[self.type] * FPS
        self.centerx = self.x + self.w / 2
        self.centery = self.y + self.h / 2
        self.atk_droprate = enemy_atkdroprate[self.type]
        self.hp_droprate = enemy_hpdroprate[self.type]

    def render(self, window):
        window.blit(self.image, (self.x, self.y))
        self.centerx, self.centery = self.x + self.w / 2, self.y + self.h / 2
        print(self.centerx, self.centery)
    def dec_health(self, dec):
        self.health_number += dec

    def check_health(self, player, HUD):
        if self.health_number <= 0:
            drop1 = random.randint(0, 100)
            drop2 = random.randint(0, 100)
            if 0 <= drop1 <= self.atk_droprate:
                object_list.append(Drop(self.centerx - 35 / 2, self.centery - 40 / 2, player, 1))
            if 0 <= drop2 <= self.hp_droprate:
                object_list.append(Drop(self.centerx - 35 / 2, self.centery - 40 / 2, player, 2))
            for wave in enemy_instances:
                if self in wave:
                    wave.remove(self)
            HUD.score_change(enemy_score[self.type])

    def stat_increase(self):
        self.damage += 1
        self.health_number += 1
        self.atk_droprate += 1
        self.speed += 1
        self.hp_droprate += 0.3
        self.speed += 1

