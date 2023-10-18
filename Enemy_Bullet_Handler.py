from Enemy_bullet import *
from Constants import *


class EnemyBulletHandler:  # Controls interactions enemy bullet-other classes
    def __init__(self, window, player):
        self.window = window
        self.player = player

    def shoot(self):
        for wave in enemy_instances:
            for enemy in wave:
                if enemy.counter <= 0 <= enemy.y + enemy.h <= Game_h:
                    if enemy.type == 0 or enemy.type == 1 or enemy.type == 2:
                        enemy_bullets.append(EnemyBullet(enemy.x + enemy.w / 2 - 7, enemy.y + enemy.h,
                                                         enemy.type, self.player.x, self.player.y))
                    elif enemy.type == 3:
                        enemy_bullets.append(EnemyBullet(enemy.x + 35, enemy.y + 25, enemy.type,
                                                         self.player.x, self.player.y))
                        enemy_bullets.append(EnemyBullet(enemy.x + 80, enemy.y + 25, enemy.type,
                                                         self.player.x, self.player.y))
                    enemy.counter = enemy_reload[enemy.type] * FPS
                enemy.counter -= 1

    def move_bullets(self):
        for bullet in enemy_bullets:
            if bullet.type == 0 or bullet.type == 1:
                bullet.move()
            if bullet.type == 2 or bullet.type == 3:
                bullet.type2move()

    def render_bullets(self):
        for bullet in enemy_bullets:
            bullet.render(self.window)

    def check_collisions(self):
        for bullet in enemy_bullets:
            if Detect_Collisions(bullet.x, bullet.y, bullet.x + bullet.w,
                                 bullet.y + bullet.h,
                                 self.player.x, self.player.y,
                                 self.player.x + self.player.w,
                                 self.player.y + self.player.h)\
                                 and bullet not in self.player.repeated_objects:
                self.player.health_number -= bullet.damage_number
                self.player.repeated_objects.append(bullet)
                enemy_bullets.remove(bullet)

    def delete_bullets(self):  # delete off-screen bullets (save memory)
        for bullet in enemy_bullets:
            '''bullet.decay -= 1
            if bullet.decay <= 0:
                enemy_bullets.remove(bullet)
                if bullet in self.player.repeated_objects:
                    self.player.repeated_objects.remove(bullet)'''
            if bullet.y > Game_h:
                if bullet in enemy_bullets:
                    enemy_bullets.remove(bullet)
                if bullet in self.player.repeated_objects:
                    self.player.repeated_objects.remove(bullet)

    def run_bullets(self):
        self.shoot()
        self.delete_bullets()
        self.move_bullets()
        self.check_collisions()
        self.delete_bullets()
        self.render_bullets()