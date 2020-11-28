# -*- coding:utf-8 -*-
"""
author: 15025
age: 26
e-mail: 1502506285@qq.com
time: 2020/11/27 17:47
software: PyCharm

Description:
"""

import pygame

# initialising python
pygame.init()
# pygame.mixer.init()
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.mixer.init()

# define display
W, H = 200, 200
HW, HH = (W / 2), (H / 2)
AREA = W * H

# initialising display
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
# pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# pygame.display.set_mode((0, 0))
FPS = 54

# define some colours
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
green = (0, 140, 0)
grey = (180, 180, 180)


class Button():

    def __init__(self, text, x=0, y=0, width=100, height=50, command=None):

        self.text = text
        self.command = command
        self.image_normal = pygame.Surface((width, height))
        self.image_normal.fill(green)
        self.image_hovered = pygame.Surface((width, height))
        self.image_hovered.fill(grey)
        self.image = self.image_normal
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.hovered = False  # is the mouse over this button?

    def update(self):
        pass

    def handleMouseOver(self, mouse_position):
        """ If the given co-ordinate inside our rect,
            Do all the mouse-hovering work             """
        # Check button position against mouse
        # Change the state *once* on entry/exit
        if self.mouseIsOver(mouse_position):
            if not self.hovered:
                # 替换图片，就不会一直判断有效了
                self.image = self.image_hovered
                self.hovered = True  # edge-triggered, not level triggered
                # Do we want to check pygame.mixer.get_busy() ?
                if not pygame.mixer.get_busy():
                    pygame.mixer.Sound(r"./musics/点击音效.mp3").play()
                    print(self.text + " DO buttonsound1.play() ")
        else:
            if self.hovered:
                self.image = self.image_normal
                self.hovered = False

    def mouseIsOver(self, mouse_position):
        """ Is the given co-ordinate inside our rect """
        return self.rect.collidepoint(mouse_position)

    def draw(self, surface):

        surface.blit(self.image, self.rect)


def main_menu():
    run = True
    btn1 = Button('Hello1', 50, 50, 40, 40)
    btn2 = Button('World2', 100, 50, 40, 40)
    btn3 = Button('Hello3', 50, 100, 40, 40)
    btn4 = Button('World4', 100, 100, 40, 40)

    # Put the buttons into a list so we can loop over them, simply
    buttons = [btn1, btn2, btn3, btn4]

    while run:

        # draw the buttons
        for b in buttons:
            b.draw(DS)  # --- draws ---

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEMOTION:
                mouse_position = event.pos
                for b in buttons:
                    b.handleMouseOver(mouse_position)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = event.pos
                for b in buttons:
                    if b.mouseIsOver(mouse_position):
                        print('Clicked:', b.text)
                        # if b.command:
                        #    b.command()

        pygame.display.update()


main_menu()
pygame.quit()
