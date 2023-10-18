from Bullet import *


class BulletHandler:  # Controls interactions between bullets and other classes
    def __init__(self, window, damage):
        self.window = window
        self.counter = 0.1 * FPS
        self.damage = damage

    def create_bullet(self, playerx, playery, delay):  # creates the bullet in the bullet list
        self.counter -= 1
        if self.counter <= 0:
            self.counter = delay
            bullet_instances.append(Bullet(playerx, playery, self.damage))

    def render_bullets(self):
        for bullet in bullet_instances:
            bullet.render(self.window)

    def check_collisions(self):
        for wave in enemy_instances:
            for enemy in wave:
                for bullet in bullet_instances:
                    if Detect_Collisions(bullet.x, bullet.y, bullet.x + bullet.w, bullet.y + bullet.w
                            , enemy.x, enemy.y, enemy.x + enemy.w, enemy.y + enemy.h) \
                            and bullet not in repeated_bullets:
                        enemy.dec_health(-self.damage)
                        repeated_bullets.append(bullet)
                        bullet_instances.remove(bullet)

    def delete_bullets(self):  # deletes off screen bullets- save memory
        for bullet in bullet_instances:
            if bullet.y < -13:
                bullet_instances.remove(bullet)

    def run_bullets(self, damage):
        self.damage = damage
        for bullet in bullet_instances:
            bullet.move()
        self.check_collisions()
        self.delete_bullets()
