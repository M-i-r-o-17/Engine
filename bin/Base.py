#
#   class[].sort(key=lambda {class_name}: {class_name}.{class_param})
#

#Самодельные вспомогательные классы
from bin.Basic import *

#Классы движка

#Библиотеки python
import pygame

class Base():

    _errorCode = "0x0"

    _count = 0
    _debug = False

    @staticmethod
    def _GetName(name = "Base"):
        return name + f" {Base._count}"

    def __new__(cls, position, size):

        Base._count += 1

        if position is None:
            Debug.ERROR(Base._errorCode, 1, f"Позиция обьекта не задана", Base._GetName())
            return None

        if not(isinstance(position, (tuple, Vector2))):
            Debug.ERROR(Base._errorCode, 2, f"Позиция обьекта имеет не правельный тип данных! Поддерживаются только Vector2 и typle", Base._GetName())
            return None

        
        if size is None:
            Debug.ERROR(Base._errorCode, 3, "Размер обьекта не задан", Base._GetName())
            return None

        if not(isinstance(size, (tuple, Vector2))):
            Debug.ERROR(Base._errorCode, 4, "Позиция имеет не правельный тип данных! Поддерживаются только Vector2 и typle", Base._GetName())
            return None
        
        return super().__new__(cls)
    
    def _CreateName(self, name = "Base"):
        self.name = name + f" {Base._count}"

    def __init__(self, position, size):

        Base._count += 1

        self.name = self._CreateName()

        self.active = True

        self.layer = 0

        self.color              = Color.color
        self.backgroundColor    = Color.background

        self.position = Vector2()
        self.size     = Vector2()

        self.surface = None
        
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

        self.drawRect = True
        self.__colorRect = self.color
        self.__marginRect = (0 + self.paddingSurface[0], 0 + self.paddingSurface[1],
                           0 + self.paddingSurface[2], 0 + self.paddingSurface[3])

    @property
    def _rect(self):
        return pygame.Rect(0 + self.__marginRect[0], 0 + self.__marginRect[1], self.size.x - self.__marginRect[2], self.size.y - self.__marginRect[3])

    #default private
    def _Draw(self, surface):

        self._surface.fill( self.backgroundColor )

        if self.drawRect: pygame.draw.rect(self._surface, self.__colorRect, self._rect)

        surface.blit(self.surface, self.position.array)

    #default public
    def Start(self):
        pass

    def Update(self, surface):
        self._Draw(surface)

    def FixedUpdate(self, surface):
        self._Draw(surface) 

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
    def SetMarginRect(self, margin):
        if len(margin) != 4: return False
        
        self.__marginRect = (margin[0] + self.paddingSurface[0], margin[1] + self.paddingSurface[1],
                           margin[2] + self.paddingSurface[2], margin[3] + self.paddingSurface[3])
        
        return True

    def SetColorRect(self, color):

        if len(color) != 3: return False

        self.__colorRect = color

        return True