from ..bin.Basic import *
from ..bin.BaseUI import BaseUI

import pygame # type: ignore

class Label(BaseUI):

    def __new__(cls, position, size):

        cls._errorCode = "2x0"
        cls._name = "Label"

        base = super().__new__(position, size)
        
        return base
    
    def __init__(self, position, size):

        BaseUI.__init__(self, position, size)

        self.text = None
        self.textColor = Color.white
        self.textBackground = Color.background

        self.smooth = 1

        self.font = Font()

    @property
    def surfaceFont(self):
        font = pygame.font.Font(self.font, self.size)
        return font.render(f"{self.text}", self.smooth, self.textColor, self.textBackground)

    @property
    def rect(self): return self.surfaceFont.get_rect()

    @property
    def widthFont(self): return self.rect.width

    @property
    def heightFont(self): return self.rect.height

    def _Draw(self):
        
        super()._Draw()
    
        self._surface.blit(self.surfaceFont, self.positionText)

