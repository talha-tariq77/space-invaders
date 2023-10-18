import pygame
from Constants import *


class Background:
    def __init__(self, initial_speed, obj_move_speed):
        self.image = pygame.image.load('Background3.png')
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.starty = -self.h + 600 + 1
        self.y = self.starty - 1
        self.x = 0
        self.initial_speed = initial_speed
        self.move_speed = self.initial_speed
        self.object_move_speed = obj_move_speed
        self.move_list = [enemy_instances, object_list]

    def render(self, window):
        window.blit(self.image, (self.x, self.y))
        self.y += self.move_speed
        if self.y >= 0:
            self.y = self.starty

    def check_on_screen(self, player):
        for wave in off_screen_enemies:
            for enemy in wave:
                if player.realy >= enemy.y >= player.realy - self.h:
                    enemy_instances.append(wave)

                    print(enemy_instances)
                    if wave in off_screen_enemies:
                        off_screen_enemies.remove(wave)

    def move_objects(self, player):
        if not enemy_instances:
            for wave in off_screen_enemies:
                for enemy in wave:
                    enemy.y += 10
        for wave in enemy_instances:
            for enemy in wave:
                if enemy.y <= Game_h / 2:
                    enemy.y += 2
                else:
                    enemy.y += 1
        for object in object_list:
            object.y += object.ymove
        player.realy -= 3

    def run(self, player):
        self.move_objects(player)
        self.check_on_screen(player)


class HUD:
    def __init__(self, display, player_health):
        self.score = 0
        self.display = display
        self.player_health = player_health
        self.score_image = pygame.font.Font('C:\\Windows\\Fonts\\dodger3.ttf', 50)
        self.render_score = self.score_image.render(str(self.score), True, (255, 165, 0))
        self.health = pygame.font.Font('C:\\Windows\\Fonts\\dodger3.ttf', 40).render(str(self.player_health), True, Green)

    def display_score(self, player_health):
        self.player_health = int(player_health)
        self.render_score = self.score_image.render(str(self.score), True, (255, 165, 0))
        self.health = pygame.font.Font('C:\\Windows\\Fonts\\dodger3.ttf', 40).render(str(self.player_health), True, (255, 0, 0))
        self.display.blit(self.render_score, (25, 25))
        self.display.blit(self.health, (0, Game_h - 40))

    def score_change(self, change):
        self.score += change

    def reset_score(self):
        self.score = 0
