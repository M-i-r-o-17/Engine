#
#   class[].sort(key=lambda {class_name}: {class_name}.{class_param})
#

#Самодельные вспомогательные классы
from bin.Basic import *

#Классы движка

#Библиотеки python
import pygame


class BaseUI(Basic):
    
    def __new__(cls, position, size):

        if cls._errorCode == None: cls._errorCode = "0x2"
        if cls._name == None: cls._name = "BaseUI"

        base = super().__new__(cls, position, size)

        return base

    def __init__(self, position, size):

        BaseUI._id += 1

        pygame.font.init()

        self.name = self._CreateName()

        self.active = True

        self.layer = 0
        
        if type(position) == Vector2:
            self.position = position
        elif type(position) == tuple:
            self.position = Vector2(position[0], position[1])

        if type(size) == Vector2:
            self.size = size
        elif type(size) == tuple:
            self.size = Vector2(size[0], size[1])

        self._surface = pygame.Surface(size.array)

        self.paddingSurface = (0, 0, 0, 0)
        
    @property
    def width(self):
        return self.size.x

    @property
    def height(self):
        return self.size.y
    