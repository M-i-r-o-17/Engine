import math

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
    def WARNING(message, name:str=None):
        if name == None:
            print(f" \033[37m\033[43m[WARNING]\033[0m \033[33m{message}\033[0m ")
        else:
            print(f" \033[37m\033[43m[WARNING in '{name}']\033[0m \033[33m{message}\033[0m ")
    
    @staticmethod
    def ERROR(prefix:str, code:int, message, name:str=None):
        if name == None:
            print(f" \033[37m\033[41m[ERROR]\033[0m \033[31mEngine code: {prefix}"+ "0" * (7 - len(f"{code}")) +f"{code}: {message}\033[0m")
        else:
            print(f" \033[37m\033[41m[ERROR in '{name}']\033[0m \033[31mEngine code: {prefix}"+ "0" * (7 - len(f"{code}")) +f"{code}: {message}\033[0m")
    def __init__(self):
        pass