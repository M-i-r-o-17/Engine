import math
import enum
import pygame # type: ignore

class Vector2():

    def __init__(self, x:int = 0, y:int = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x:{self.x} y:{self.y}"
        
    def __repr__(self):
        return f"Vector2({str(self)})"
    
    def __add__(self, value): 
        return Vector2(self.x + value.x, self.y + value.y)
        
    def __mul__(self, value): 
        return Vector2(self.x * value.x, self.y * value.y)
        
    def __neg__(self):
        return Vector2(-self.x,-self.y)
        
    def __sub__(self, value, /):
        return Vector2(self.x - value.x, self.y - value.y)
        
    def __truediv__(self, value):
        return Vector2(self.x // value.x, self.y // value.y) 
    
    def distance(self, vector):
        return math.sqrt((vector.x - self.x)**2 + (vector.y - self.y) ** 2)
    
    @property
    def right(self):
        return Vector2(1, 0)
    @property
    def left(self):
        return Vector2(-1, 0)
    @property
    def up(self):
        return Vector2(0, 1)
    @property
    def down(self):
        return Vector2(0, -1)
    @property
    def zero(self):
        return Vector2(0, 0)
    @property
    def array(self):
        return (self.x, self.y)

class Color():

    background      = (10, 10, 10)

    color           = (90, 90, 90)

    selectColor     = (60, 60, 60)

    activeColor     = (30, 30, 30)

    white           = (255, 255, 255)

    black           = (0, 0, 0)

    def __init__(self):
        pass  

class Debug():

    @staticmethod
    def LOG(message, name:str=None):
        if name == None:
            print(f" \033[30m\033[47m[LOG]\033[0m {message}\033[0m ")
        else:
            print(f" \033[30m\033[47m[LOG in '{name}']\033[0m {message}\033[0m ")
    
    @staticmethod
    def WARNING(message, prefix:str = "", code:int = None,name:str=None):
        warning = "[WARNING]"
        if name != None: warning = f"[WARNING in '{name}']"
        warCode = ""
        if code != None: warCode = f"Engine code: {prefix}"+ "0" * (6 - len(f"{code}")) + f"{code}: "

        print(f" \033[37m\033[43m{warning}\033[0m \033[33m{warCode}{message}\033[0m ")
    
    @staticmethod
    def ERROR(prefix:str, code:int, message, name:str=None):
        if name == None:
            print(f" \033[37m\033[41m[ERROR]\033[0m \033[31mEngine code: {prefix}"+ "0" * (6 - len(f"{code}")) +f"{code}: {message}\033[0m")
        else:
            print(f" \033[37m\033[41m[ERROR in '{name}']\033[0m \033[31mEngine code: {prefix}"+ "0" * (6 - len(f"{code}")) +f"{code}: {message}\033[0m")
    def __init__(self):
        pass

class Basic():
    _errorCode = "0x0"

    _id = 0
    _debug = False
    
    def __new__(cls, position, size):

        if cls._name == None: cls._name = "Basic"
        if cls._errorCode == None: cls._errorCode = "0x0"

        if position is None:
            Debug.ERROR(cls._errorCode, 1, f"Позиция сущности не задана", cls._name + f" {cls._id}")
            return None

        if not(isinstance(position, (tuple, Vector2))):
            Debug.ERROR(cls._errorCode, 2, f"Позиция сущности имеет не правельный тип данных! Поддерживаются только Vector2 и typle", cls._name + f" {cls._id}")
            return None

        
        if size is None:
            Debug.ERROR(cls._errorCode, 3, "Размер сущности не задан", cls._name + f" {cls._id}")
            return None

        if not(isinstance(size, (tuple, Vector2))):
            Debug.ERROR(cls._errorCode, 4, "Позиция сущности имеет не правельный тип данных! Поддерживаются только Vector2 и typle", cls._name + f" {cls._id}")
            return None
        
        cls._id += 1

        return super().__new__(cls)

    def _CreateName(self, name = "Basic"):
        self.name = name + f" {Basic._id}"

    def __init__(self, position, size):

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
    
    #default private
    def _Draw(self):
        self._surface.fill( self.backgroundColor )

    #default public
    def Start(self):
        pass

    def Update(self, surface):
        self._Draw()
        surface.blit(self._surface, self.position.array)

    def FixedUpdate(self, surface):
        self._Draw()
        surface.blit(self._surface, self.position.array) 

class AliginFont(enum.Enum):

    rightTop        = 2
    middleTop       = 1
    leftTop         = 0

    rightMidle      = 5
    center          = 4
    leftMiddle      = 3

    rightBottom     = 8
    middleBottom    = 7
    leftBottom      = 6

class Font():

    defaultPath = "Engine/UI/font/"

    fontRegular     = "Menlo-Regular.ttf"
    fontItalic      = "Menlo-Italic.ttf"
    fontBoldItalic  = "Menlo-BoldItalic.ttf"
    fontBold        = "Menlo-Bold.ttf"

    def __init__(self, bold:bool = False, italic:bool = False, path:str = None, size:int = 16, aligin:AliginFont = AliginFont.leftTop):

        self.bold   = bold
        self.italic = italic

        self.path = path

        self.size = size

        self.aligin = aligin

    @property
    def font(self):
        if self.path != None: return self.path

        if self.bold and self.italic:
            return self.defaultPath + self.fontBoldItalic
        elif self.bold:
            return self.defaultPath + self.fontBold
        elif self.italic:
            return self.defaultPath + self.fontItalic
        else:
            return self.defaultPath + self.fontItalic