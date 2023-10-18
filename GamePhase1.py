import pygame
from Constants import *

reset_switch = False
def display_text(text, window, x, y):
    font = pygame.font.Font('C:\\Windows\\Fonts\\dodger3.ttf', 155)
    text_obj = font.render(text, True, Red)
    x -= text_obj.get_rect().w / 2
    y -= text_obj.get_rect().h / 2
    window.blit(text_obj, (x, y))

pygame.font.init()
bigdodger = pygame.font.Font('C:\\Windows\\Fonts\\dodger3.ttf', 155)
mediumdodger = pygame.font.Font('C:\\Windows\\Fonts\\dodger3.ttf', 100)


class ButtonObj:
    def __init__(self, name, text, x, y, colour, font, window):
        self.name = name
        self.window = window
        self.x = x
        self.y = y
        self.colour = colour
        self.text = text
        self.fontstyle = font
        self.font = self.fontstyle.render(self.text, True, self.colour)
        self.w = self.font.get_rect().w
        self.h = self.font.get_rect().h

        self.x -= self.w / 2
        self.y -= self.h / 2
        button_list.append(self)

    def render(self):
        self.window.blit(self.font, (self.x, self.y))

    def pressed(self, mousex, mousey):
        if Detect_Collisions(self.x, self.y, self.x + self.w, self.y + self.h, mousex, mousey, mousex, mousey):
            return True
        else:
            return False


class GamePhase:
    def __init__(self, window):
        self.window = window
        self.create_buttons()

    def create_buttons(self):
        button_list.clear()
        if Game_switches['Intro-screen']:
            play_button = ButtonObj('play', 'Play', Game_w / 2, Game_h / 2, Red, pygame.font.Font('C:\\Windows\\Fonts\\dodger3.ttf', 100), self.window)
            instruction_button = ButtonObj('instructions-button', 'Instructions', Game_w / 2, 500, Red, pygame.font.Font('C:\\Windows\\Fonts\\dodger3.ttf', 60), self.window)
        if Game_switches['End-screen'] == 'Lost':
            loss = ButtonObj('lost', 'Lost', Game_w / 2, Game_h / 2, Red, pygame.font.Font('C:\\Windows\\Fonts\\dodger3.ttf', 100), self.window)
        if Game_switches['End-screen'] == 'Won':
            won = ButtonObj('won','Won', Game_w / 2, Game_h / 2, Red, pygame.font.Font('C:\\Windows\\Fonts\\dodger3.ttf', 100), self.window)
        if Game_switches['End-screen'] == 'Lost' or Game_switches['End-screen'] == 'Won':
            play_again = ButtonObj('play again','Play again', Game_w / 2, Game_h / 2 + 100, Red, pygame.font.Font('C:\\Windows\\Fonts\\dodger3.ttf', 60), self.window)
        if Game_switches['Instructions-screen']:
            instructions = ButtonObj('instructions', '''asdf/arrowkeys to move, space to shoot''', Game_w / 2, Game_h / 2, Red, pygame.font.Font('C:\\Windows\\Fonts\\dodger3.ttf', 25), self.window)
            back = ButtonObj('back-button', 'Back', 40, 20, Green, pygame.font.Font('C:\\Windows\\Fonts\\dodger3.ttf', 20), self.window)

    def handle_collisions(self, mousex, mousey):
        if Game_switches['Intro-screen']:
            for button in button_list:
                if button.name == 'play' and button.pressed(mousex, mousey):
                    Game_switches['Intro-screen'] = False
                    Game_switches['Game-screen'] = True
                    self.create_buttons()
                    return 'make lvl'
                if button.name == 'instructions-button' and button.pressed(mousex, mousey):
                    Game_switches['Instructions-screen'] = True
                    Game_switches['Intro-screen'] = False
                    self.create_buttons()
        if Game_switches['Instructions-screen']:
            for button in button_list:
                if button.name == 'back-button' and button.pressed(mousex, mousey):
                    Game_switches['Intro-screen'] = True
                    Game_switches['Instructions-screen'] = False
                    self.create_buttons()
        if Game_switches['End-screen'] == 'Lost' or Game_switches['End-screen'] == 'Won':
            for button in button_list:
                if button.name == 'play again' and button.pressed(mousex, mousey):
                    Game_switches['End-screen'] = False
                    Game_switches['Intro-screen'] = True
                    self.create_buttons()
                    return 'make lvl'

    def handle_events(self):
        mousex, mousey = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_collisions(mousex, mousey)

    def render(self):
        self.window.fill(White)
        for button in button_list:
            button.render()
        pygame.display.update()

    def run(self):
        self.handle_events()
        self.render()
