'''Final project
Winter 2017
author Sebrina Zeleke(stz4)
'''


from tkinter import *
from falling_from_the_top import *
canv_dim = 600

class Apple(Falling_object):
    def __init__(self,canvas, x , y , vel):
        '''initialize values'''
        Falling_object.__init__(self,canvas,x,y)
        self._img_apple = PhotoImage(file = 'giphy(1).gif')
        self._vel = vel
        
    def create(self):
        '''create apple'''
        self._canvas.create_image(self._x,self._y, image = self._img_apple, tag = "apple")
    


    