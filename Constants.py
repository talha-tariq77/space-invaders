Game_w = 800
Game_h = 600

FPS = 60

score_number = 0

# Color types
White = (255, 255, 255)
Black = (0, 0, 0)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)

Player_start_x = 40
Player_start_y = 215

Game_switches = {'Intro-screen': True, 'Instructions-screen': False, 'Game-screen': False, 'End-screen': False}


Bullet_w = 13
bullet_instances = []
repeated_bullets = []  # Stores bullets intercepted by an Enemy

# Enemy-Type Data:
enemy_instances = []
off_screen_enemies = []
enemy_images = ['enemy.png', 'enemy.png', 'Enemy2.png', 'Enemy2.png']
enemy_health = [80, 90, 150, 200]
enemy_damage = [6, 8, 2, 1]
enemy_reload = [1, 1, 2, 2]  # reload in secs
enemy_atkdroprate = [50, 20, 30, 30]
enemy_hpdroprate = [30, 15, 20, 30]
enemy_score = [10, 20, 20, 130]
object_list = []
button_list = []

enemy_bullets = []
bullet_speed = [8, 7, 3, 3]
bullet_damage = [3, 3, 7, 5, 4]
bullet_images = ['enemy bullet.png', 'enemy bullet.png', 'enemy type 2 bullet.png', 'enemy type 2 bullet.png', 'enemy bullet.png']

render_objects = []


def Detect_Collisions(Ax, Ay, AX, AY, Bx, By, BX, BY):  # Function checks if two objects are colliding
    if not (AX < Bx or BX < Ax or AY < By or BY < Ay):
        return True
