from p5 import *

class Tile:

    _x=0
    _y=0
    _color=0

    def __init__ (self,x,y):
        self._x=x
        self._y=y
        self.color= Color(255,0,0)

    
    def Draw(self):
        fill(self.color)
        rect((self._x,self._y),100,100)