# -*- coding:utf-8 -*-
"""
author: 15025
age: 26
e-mail: 1502506285@qq.com
time: 2020/11/28 14:06
software: PyCharm

Description:
"""
import pygame
import sys
import random
import time
import os

version = "v1.00"


class MainGame:
    # the size of game window
    __SCREEN_WIDTH = 1000
    __SCREEN_HEIGHT = 800

    window = None

    def __init__(self):
        # to make the main windows be opened always at the center of screen
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        # initialize modules of pygame
        pygame.init()
        # set window size of game
        MainGame.window = pygame.display.set_mode([MainGame.__SCREEN_WIDTH, MainGame.__SCREEN_HEIGHT])
        # set caption of window
        pygame.display.set_caption('My Life ' + version)

    def mainGame(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.displayImage()
            pygame.display.update()

    def displayImage(self):
        directory = [r"./materials/机器猫头左.png", r"./materials/机器猫头中.png", r"./materials/机器猫头右.png"]
        image = pygame.image.load(directory[random.randint(0, 2)])
        MainGame.window.fill((0, 0, 0), (100, 100, 166, 152))
        MainGame.window.fill((255, 0, 0), (200, 200, 266, 252))
        MainGame.window.blit(image, (100, 100))
        time.sleep(2)


if __name__ == "__main__":
    # ML for My Life
    game_ML = MainGame()
    game_ML.mainGame()
