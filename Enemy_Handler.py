from Enemy import *
from Constants import *
import random


class EnemyHandler:  # Controls interactions between Enemy - Other Classes
    def __init__(self, window, player, HUD):
        self.window = window
        self.right = True
        self.player = player
        self.HUD = HUD

    def movement_algorithm(self):
        for wave in enemy_instances:
            for enemy in wave:
                if enemy.type == 1:
                    if enemy.x >= Game_w - enemy.w:
                        enemy.right = False
                    elif enemy.x <= 0:
                        enemy.right = True
                    if enemy.right:
                        enemy.x += 1 * enemy.speed
                    else:
                        enemy.x -= 1 * enemy.speed

    def render(self):
        for object in object_list:
            object.render(self.window)
        for wave in enemy_instances:
            for enemy in wave:
                enemy.render(self.window)

    def check_health(self):
        for wave in enemy_instances:
            for enemy in wave:
                enemy.check_health(self.player, self.HUD)


    def drop_check(self):
        for object in object_list:
            object.collisions(self.player)

    def run(self):
        self.check_health()
        self.movement_algorithm()
        self.drop_check()
        self.render()
