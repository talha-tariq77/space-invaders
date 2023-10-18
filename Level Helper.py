import pygame
pygame.init()
Game_w = 800
Game_h = 600
level_width = 800
level_height = 900
screen_w = 800
screen_h = 600
zoom_width = level_width
zoom_height = level_height
scalex = zoom_width / screen_w
scaley = zoom_height / screen_h

enscalex = scaley / 3 * 4
display = pygame.display.set_mode((screen_w, screen_h), pygame.RESIZABLE)
type1 = []
type2 = []
type3 = []
type4 = []
types = [type1, type2, type3, type4]
active = None
type_colours = [(244, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255)]

border_images = []

border = pygame.Surface((30, 1))
border.fill((100, 100, 100))
for i in range(int(level_height / Game_h)):
    border_images.append(border)

class Image:
    def __init__(self, x, y, image, type):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.type = type
        self.transform()

    def render(self):
        display.blit(self.image, (self.x, self.y))

    def transform(self):
        self.image = pygame.Surface((self.w / scalex, self.h / scaley))
        self.image.fill(type_colours[self.type])
        self.w = self.image.get_width()
        self.h = self.image.get_height()

enemy_images = ['enemy.png', 'enemy.png', 'Enemy2.png', 'Enemy2.png']
blit_images = [[]]
screen_val = 1
max_screen = 1
while True:
    mousex, mousey = pygame.mouse.get_pos()
    for event in pygame.event.get():
        active_key = pygame.key.get_pressed()
        if active_key[pygame.K_1]:
            active = 0
        if active_key[pygame.K_2]:
            active = 1
        if active_key[pygame.K_3]:
            active = 2
        if active_key[pygame.K_4]:
            active = 3
        if active_key[pygame.K_SPACE]:
            active = None
        if active_key[pygame.K_RIGHT]:
            screen_val += 1
            max_screen += 1
            blit_images.append([])
            print('screen val', screen_val)
        if active_key[pygame.K_LEFT]:
            screen_val -= 1
            blit_images.append([])
            print('screen val', screen_val)
        if event.type == pygame.MOUSEBUTTONDOWN:
            for type in types:
                while len(type) < max_screen:
                    type.append([])
                    print(type)
            realx, realy = mousex * scalex, -1 * mousey * scaley
            print(realx, realy)
            for i in range(4):
                if active == i:
                    blit_images[screen_val - 1].append(Image(mousex, mousey, enemy_images[i], i))
                    types[i][screen_val - 1].append((realx, realy * screen_val))
            print(type1, '\n', type2, '\n', type3, '\n', type4)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.VIDEORESIZE:
            screen_w, screen_h = event.w, event.h
            display = pygame.display.set_mode((screen_w, screen_h), pygame.RESIZABLE)
            print(screen_w, screen_h)
        if active_key[pygame.K_h]:
            resize = int(input('screen w: ')), int(input('screen h: '))
            screen_w, screen_h = resize
            print(screen_w, screen_h)
            display = pygame.display.set_mode((screen_w, screen_h), pygame.RESIZABLE)
        if active_key[pygame.K_BACKSPACE]:
            for i in range(4):
                if (blit_images[screen_val - 1][-1].x, blit_images[screen_val - 1][-1].y) in types[i]:
                    types[i].remove((blit_images[screen_val - 1][-1].x, blit_images[screen_val - 1][-1].y))
            blit_images[screen_val - 1].remove(blit_images[screen_val - 1][-1])
    display.fill((0, 0, 0))
    if blit_images:
        for image in blit_images[screen_val - 1]:
            image.render()
    for i in range(len(border_images)):
        display.blit(border_images[i], (0, i * Game_h / scaley))
    pygame.display.update()
