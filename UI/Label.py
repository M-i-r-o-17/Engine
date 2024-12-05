from bin.Basic import *
from bin.BaseUI import BaseUI

import pygame

class Label(BaseUI):

    def __new__(cls, position, size):

        cls._errorCode = "0x4"
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
        
        position = Vector2()

        if self.font.aligin is AliginFont.leftTop:
            position = Vector2(self.position.x + self.paddingSurface[0], self.position.y)
        if self.font.aligin  is AliginFont.middleTop:
            position = Vector2(self.position.x + (self.width - self.paddingSurface[0] - self.paddingSurface[2]) // 2 + self.widthFont // 2, self.position.y)
        if self.font.aligin  is AliginFont.rightTop:
            position = Vector2(self.position.x + (self.width - self.widthFont - self.paddingSurface[2]), self.position.y)
        if self.font.aligin  is AliginFont.leftMiddle:
            position = Vector2(self.position.x + self.paddingSurface[0], self.position.y + (self.height // 2 - self.heightFont // 2 + self.paddingSurface[1]))
        if self.font.aligin  is AliginFont.center:
            position = Vector2(self.position.x + (self.width - self.paddingSurface[0] - self.paddingSurface[2]) // 2 + self.widthFont // 2, self.position.y, self.position.y + (self.height // 2 - self.heightFont // 2 + self.paddingSurface[1]))
        if self.font.aligin  is AliginFont.rightMidle:
            position = Vector2(self.position.x + (self.width - self.widthFont - self.paddingSurface[2]), self.position.y + (self.height // 2 - self.heightFont // 2 + self.paddingSurface[1]))
        if self.font.aligin  is AliginFont.leftBottom:
            position = Vector2(self.position.x + self.paddingSurface[0], self.height - self.heightFont - self.paddingSurface[3])
        if self.font.aligin  is AliginFont.middleBottom:
            position = Vector2(self.position.x + (self.width - self.paddingSurface[0] - self.paddingSurface[2]) // 2 + self.widthFont // 2, self.height - self.heightFont - self.paddingSurface[3])
        if self.font.aligin  is AliginFont.rightBottom:
            position = Vector2(self.position.x + (self.width - self.widthFont - self.paddingSurface[2]), self.height - self.heightFont - self.paddingSurface[3])


        self._surface.blit(self.surfaceFont, position.array)

