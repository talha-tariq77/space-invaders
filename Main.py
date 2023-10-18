from Player import *
from Bullet_Handler import *
from Enemy_Handler import *
from Enemy_Bullet_Handler import *
from Background import *
from GamePhase1 import *
pygame.init()

print(''' THIS GAME AND ALL ITS ASSETS WERE CREATED BY TALHA ARSLAN TARIQ \n
THIS IS A SAMPLE OF THE FULL GAME\n
FOR ANY PROBLEMS LAUNCHING OR PLAYING, PLEASE SEE THE 'READ ME' FILE
''')


class Game:
    def __init__(self):
        self.reset_switch = False
        self.window = pygame.display.set_mode((Game_w, Game_h))
        pygame.display.set_caption("Talha's Game ")
        self.player = Player()
        self.HUD = HUD(self.window, self.player.health_number)
        self.bullet_handler = BulletHandler(self.window, self.player.damage)
        self.clock = pygame.time.Clock()
        self.enemy_handler = EnemyHandler(self.window, self.player, self.HUD)
        self.enemy_bullet_handler = EnemyBulletHandler(self.window, self.player)
        self.background = Background(0.5, 3)
        self.Phase = GamePhase(self.window)
        self.stat_increase = 0
        self.level(1)
        self.smallfont = pygame.font.Font('C:\\Windows\\Fonts\\dodger3.ttf', 50)

    def render(self):
        self.background.render(self.window)
        self.player.render(self.window)
        self.enemy_handler.render()
        self.bullet_handler.render_bullets()
        self.enemy_bullet_handler.render_bullets()
        self.HUD.display_score(self.player.health_number)
        pygame.display.update()

    def passive_increase(self):
        self.stat_increase -= 1
        if self.stat_increase <= 0:
            self.player.health_number += .1
            self.player.damage += 0.1
            self.stat_increase = self.norm_stat_increase

    def run(self):
        self.bullet_handler.run_bullets(self.player.damage)
        self.enemy_handler.run()
        self.enemy_bullet_handler.run_bullets()
        self.background.run(self.player)
        self.passive_increase()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        active_key = pygame.key.get_pressed()
        if active_key[pygame.K_UP] or active_key[pygame.K_w]:
            self.player.move(0, -1)
            self.player.yspeed = 3
        else:
            self.player.yspeed = 4
        if active_key[pygame.K_DOWN] or active_key[pygame.K_s]:
            self.player.move(0, 1)
            self.player.yspeed = 4
        else:
            self.player.yspeed = 3
        if active_key[pygame.K_LEFT] or active_key[pygame.K_a]:
            self.player.move(-1, 0)
        if active_key[pygame.K_RIGHT] or active_key[pygame.K_d]:
            self.player.move(1, 0)
        if active_key[pygame.K_SPACE]:
            self.bullet_handler.create_bullet(self.player.x + self.player.w / 2 - Bullet_w / 2, self.player.y, self.player.bullet_delay)

    def active_loop(self):
        while True:
            if not Game_switches['Game-screen']:
                self.Phase.run()

            if Game_switches['Game-screen']:
                self.handle_events()
                self.run()
                self.render()

                def wave_check():
                    for wave in off_screen_enemies:
                        if wave:
                            return False
                def instance_check():
                    for wave in enemy_instances:
                        if wave:
                            return False
                if self.player.health_number == 1:
                    Game_switches['Game-screen'] = False
                    Game_switches['End-screen'] = 'Lost'
                    self.Phase.create_buttons()
                    self.player.health_number = 100
                    self.reset()
                elif instance_check() != False and wave_check() != False:
                    Game_switches['Game-screen'] = False
                    Game_switches['End-screen'] = 'Won'
                    self.Phase.create_buttons()
                    self.level(1)
                    self.reset()

    def reset(self):
        off_screen_enemies.clear()
        self.player.x = 100
        self.player.y = Game_h - self.player.h
        self.player.health_number = 100
        self.player.__init__()
        object_list.clear()
        enemy_instances.clear()
        bullet_instances.clear()
        enemy_bullets.clear()
        self.level(1)
        self.HUD.reset_score()
        self.reset_switch = True
        # RESET FUNCTION FOR ALL OBJECTS AND CLASSES

    def level(self, lvl):
        off_screen_enemies.clear()
        self.wave_len = 0
        def addtype(type, *args):
            if len(args) > self.wave_len:
                self.wave_len = len(args)
                for i in range(self.wave_len - len(off_screen_enemies)):
                    off_screen_enemies.append([])
            for list in args:
                for wave in list:
                    for tuple in wave:
                        off_screen_enemies[args.index(list)].append(Enemy(tuple[0] * 10, tuple[1] * 10, type))
        if self.reset_switch == True:

            addtype(1, [[400, -400]])
            self.reset_switch = False

        if lvl == 1:  # LVL NEEDS TO BE ADDED INTO LISTS AGAIN AFTER 'PLAY AGAIN' IS CLICKED!
            self.norm_stat_increase = 2 * FPS
            self.stat_increase = self.norm_stat_increase
            addtype(1, [[(142.0, -676.5), (569.0, -649.5), (351.0, -658.5)],
                        [(111.0, -1485.0), (369.0, -1473.0), (616.0, -1479.0), (364.0, -867.0), (586.0, -342.0),
                         (213.0, -294.0),
                         (390.0, -111.0)], [(190.0, -954.0), (546.0, -1035.0), (38.0, -1521.0), (707.0, -1566.0)],
                        [(571.0, -2274.0), (402.0, -2820.0), (264.0, -2202.0), (53.0, -2154.0), (736.0, -2208.0)],
                        [(330.0, -900.0), (406.0, -3795.0)], [(100.0, -702.0), (357.0, -702.0), (639.0, -774.0)], [],
                        [(107.0, -948.0), (692.0, -900.0)], [(395.0, -5818.5), (722.0, -5602.5), (53.0, -5602.5)], [],
                        [], [],
                        [(58.0, -8502.0), (256.0, -9711.0), (502.0, -9613.5), (710.0, -7507.5)], [], []])
            addtype(2, [[], [], [(589.0, -958.5), (158.0, -1057.5), (378.0, -2007.0), (413.0, -220.5)],
                        [(132.0, -510.0), (656.0, -552.0), (410.0, -1296.0)],
                        [(370.0, -2160.0), (667.0, -2182.5), (91.0, -2542.5)],
                        [(41.0, -3708.0), (717.0, -3699.0), (383.0, -2493.0)], [(645.0, -3790.5), (104.0, -3654.0)],
                        [(62.0, -6036.0), (302.0, -4164.0), (419.0, -3096.0), (594.0, -4440.0), (714.0, -6600.0)], [],
                        [(130.0, -6795.0), (402.0, -6930.0), (693.0, -7200.0), (564.0, -5475.0), (294.0, -4740.0),
                         (387.0, -2400.0)], [(135.0, -8481.0), (559.0, -8629.5)], [(178.0, -7722.0), (528.0, -9234.0)],
                        [], [],
                        [(39.0, -2947.5), (142.0, -5557.5), (269.0, -7537.5), (397.0, -9450.0), (567.0, -7267.5),
                         (614.0, -4905.0),
                         (693.0, -2452.5), (397.0, -1777.5)]])
            addtype(3, [[], [], [], [], [], [], [(373.0, -1333.5)], [], [(135.0, -1876.5), (522.0, -2133.0)],
                        [(641.0, -2070.0), (102.0, -2070.0)],
                        [(41.0, -5230.5), (634.0, -5263.5), (353.0, -4735.5), (295.0, -1452.0)], [], [], [], []])
            addtype(4, [[], [], [], [], [], [], [], [], [], [], [], [(154.0, -3258.0), (556.0, -3222.0)], [],
                        [(92.0, -2121.0), (570.0, -1764.0), (410.0, -6615.0), (249.0, -6783.0)], [(374.0, -4927.5)]])
game = Game()
game.active_loop()

