from bin.Basic import *
from bin.Base import Base

import pygame # type: ignore

class Transform(Base):

    def __new__(cls, position, size):

        cls._errorCode = "1x0"
        cls._name = "Transform"

        base = super().__new__(cls,position, size)

        return base
    
    def __init__(self, position, size):

        Base.__init__(self, position, size)

        self.OnCollisionEnterEvent = None
        self.OnCollisionEvent      = None
        self.OnCollsionExitEvent   = None

        print(f"{self._id=} | {self._name}")

    @property
    def width(self):
        return self.size.x

    @property
    def height(self):
        return self.size.y

    @property
    def left(self):
        return Vector2(self.position.x, self.position.y + self.height // 2)

    @property
    def right(self):
        return Vector2(self.position.x + self.width, self.position.y + self.height // 2)

    @property
    def top(self):
        return Vector2(self.position.x + self.width // 2, self.position.y)

    @property
    def bottom(self):
        return Vector2(self.position.x + self.width // 2, self.position.y + self.height)

    @property
    def center(self):
        return Vector2(self.position.x + self.width // 2, self.position.y + self.height // 2)

    def OnCollisionEnter(self, transform):
        if   self.left.distance(transform.right) <= 0.01:
            if self.OnCollisionEnterEvent != None: self.OnCollisionEnterEvent()
            else: Debug.WARNING("Не установлен метод коллизи при сопрекосновении по умолчанию!", Transform._errorCode, 1001, Transform._name)
            return True
        elif self.right.distance(transform.left) <= 0.01:
            if self.OnCollisionEnterEvent != None: self.OnCollisionEnterEvent()
            else: Debug.WARNING("Не установлен метод коллизи при сопрекосновении по умолчанию!", Transform._errorCode, 1001, Transform._name)
            return True
        elif self.top.distance(transform.bottom) <= 0.01:
            if self.OnCollisionEnterEvent != None: self.OnCollisionEnterEvent()
            else: Debug.WARNING("Не установлен метод коллизи при сопрекосновении по умолчанию!", Transform._errorCode, 1001, Transform._name)
            return True
        elif self.bottom.distance(transform.top) <= 0.01:
            if self.OnCollisionEnterEvent != None: self.OnCollisionEnterEvent()
            else: Debug.WARNING("Не установлен метод коллизи при сопрекосновении по умолчанию!", Transform._errorCode, 1001, Transform._name)
            return True 
        else: return False
    
    def OnCollision(self, transform):
        if   self.center.distance(transform.right)    <= self.width // 2:  
            if self.OnCollisionEvent != None: self.OnCollisionEvent()
            else: Debug.WARNING("Не установлен метод коллизи по умолчанию!", Transform._errorCode, 1000, Transform._name)
            return True
        elif self.center.distance(transform.left)     <= self.width // 2: 
            if self.OnCollisionEvent != None: self.OnCollisionEvent() 
            else: Debug.WARNING("Не установлен метод коллизи по умолчанию!", Transform._errorCode, 1000, Transform._name)
            return True
        elif self.center.distance(transform.top)      <= self.height // 2:
            if self.OnCollisionEvent != None: self.OnCollisionEvent() 
            else: Debug.WARNING("Не установлен метод коллизи по умолчанию!", Transform._errorCode, 1000, Transform._name)
            return True
        elif self.center.distance(transform.bottom)   <= self.height // 2: 
            if self.OnCollisionEvent != None: self.OnCollisionEvent()
            else: Debug.WARNING("Не установлен метод коллизи по умолчанию!", Transform._errorCode, 1000, Transform._name)
            return True
        else: return False

    def CollisionEvent(self):
        if self.OnCollisionEvent != None: self.OnCollisionEvent()
        else: Debug.WARNING("Не установлен метод коллизи по умолчанию!", Transform._errorCode, 100, Transform._name)
    
    def Move(self, dx, dy):
        self.position += Vector2(dx, dy)

    def MoveToVector(self, position:Vector2):
        self.position += position

    def MoveToDx(self, dx):
        self.position += Vector2(dx, 0)

    def MoveToDy(self, dy):
        self.position += Vector2(0, dy)

