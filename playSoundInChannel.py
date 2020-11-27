# -*- coding:utf-8 -*-
"""
author: 15025
age: 26
e-mail: 1502506285@qq.com
time: 2020/11/27 13:46
software: PyCharm

Description:
"""
import pygame
import os
import sys

version = 'v1.00'


class MainGame:
    # the size of game window
    __SCREEN_WIDTH = 640
    __SCREEN_HEIGHT = 480

    __FULLSCREEN = False

    def __init__(self):
        # to make the main windows be opened always at the center of screen
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        # initialize modules of pygame
        pygame.init()
        # set window size of game
        MainGame.window = pygame.display.set_mode([MainGame.__SCREEN_WIDTH, MainGame.__SCREEN_HEIGHT])
        # set caption of window
        pygame.display.set_caption('My Life ' + version)

        self.playSound()

    @staticmethod
    def mainGame():
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

    @staticmethod
    def playSound():
        pygame.mixer.Channel(0).play(pygame.mixer.Sound(r"./musics/逍遥传说.mp3"))


if __name__ == "__main__":
    game_ML = MainGame()
    game_ML.mainGame()
