from bin.Basic import *
from bin.Base import Base

import pygame # type: ignore

class Sprite(Base):

    def __new__(cls, position, size, path, convertAlpha):

        cls._errorCode = "0x5"
        cls._name = "Sprite"

        base = super().__new__(cls,position, size)

        if path == "":
            Debug.WARNING("Путь не задан", cls._errorCode, 5, cls._name)
            base = None

        return base

    def __init__(self, position, size, path:str = "", convertAlpha = False, ):

        Base.__init__(self, position, size)
        
        try:
            self.image = pygame.image.load(path)
        except:
            Debug.ERROR(self._errorCode, 6, "Не найдена картинка по данному пути", self._name)
            return None
        
        if convertAlpha:
            self.image = self.image.convert_alpha()
        else:
            self.image = self.image.convert()

        self.Resize(size)

    def Resize(self, size:Vector2):
        self.image = pygame.transform.scale(self.image, size.array)

    @property
    def imageSurface(self):
        return self.image


        