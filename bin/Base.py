#
#   class[].sort(key=lambda {class_name}: {class_name}.{class_param})
#

#Самодельные вспомогательные классы
from bin.Basic import *

#Классы движка

#Библиотеки python
import pygame

class Base(Basic):

    def __new__(cls, position, size):

        if cls._errorCode == None: cls._errorCode = "0x1"
        if cls._name == None:  cls._name = "Base"

        base = super().__new__(cls, position, size)
        
        return base

    def __init__(self, position, size):

        Base._id += 1

        self.name = self._CreateName()

        self.active = True

        self.layer = 0

        self.color              = Color.color
        self.backgroundColor    = Color.background

        self.position = Vector2()
        self.size     = Vector2()
        
        if type(position) == Vector2:
            self.position = position
        elif type(position) == tuple:
            self.position = Vector2(position[0], position[1])

        if type(size) == Vector2:
            self.size = size
        elif type(size) == tuple:
            self.size = Vector2(size[0], size[1])

        self.drawRect = True
        self.__colorRect = self.color

        
    @property
    def _rect(self):
        return pygame.Rect(0 , 0 , self.size.x , self.size.y)

    #default private
    def _Draw(self):

        super()._Draw()
        if self.drawRect: pygame.draw.rect(self._surface, self.__colorRect, self._rect)

    #surface
    def ResizeSurface(self, size):

        if type(size) == Vector2:
            self.size = size
        elif type(size) == tuple:
            self.size = Vector2(size[0], size[1])
        else: return False

        self.surface = pygame.Surface(size.array)

        return True

    #rect
    def SetColorRect(self, color):

        if len(color) != 3: return False

        self.__colorRect = color

        return True