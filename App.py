from .bin.Basic import *
from .bin.Base  import *
from .Transform import *
from .UI.Label  import *

import pygame # type: ignore
import sys

class App():

    def __init__(self, main = None, caption:str = "New app", size:Vector2 = Vector2(900,600), fps:int = 60):

        self.caption = caption
        self.size    = size
        self.fps     = fps

        self.DEBUG = False
        
        self.interfaceObjects = []
        self.gameObjects      = []

        self.main = main

        self.__clock = pygame.time.Clock()

        self.__screen = None

        pygame.init()
        pygame.display.set_caption(self.caption)
        self.__screen = pygame.display.set_mode(self.size.array)

    def __start(self):

        self.__screen.fill(Color.background)

        for item in self.interfaceObjects:
            self.gameObjects.append(item)

        if len(self.gameObjects) > 0:
            for object in self.gameObjects:
                object.DEBUG = self.DEBUG
                object.Start()

        self.__clock.tick(self.fps)
        pygame.display.update()

        if self.main == None:
            Debug.WARNING("Нет главного игрового цикла", "9x9", 1)
        
    def mainloop(self):
        
        self.__start()

        while True:

            self.__screen.fill(Color.background)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for element in self.interfaceObjects:
                        element.OnClick(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if len(self.gameObjects) > 0:
                for object in self.gameObjects:
                    object.Update(self.__screen)

            if isinstance(self.main, function): self.main()

            self.__clock.tick(self.fps)
            pygame.display.update()

    def addGameObject(self, object):
        self.gameObjects.append(object)

    def addInterfaceObject(self, object):
        self.interfaceObjects.append(object)     