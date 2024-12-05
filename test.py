from bin.Basic import *
from Transform import Transform

b1 = Transform((2,2), Vector2(3,3))
b2 = Transform((2,2), Vector2(3,3))

b1.OnCollision(b2)