'''Final project
Winter 2017
author Sebrina Zeleke(stz4)
'''

from tkinter import *
from falling_from_the_top import *

class Orange(Falling_object):
    '''initializes values'''
    def __init__(self,canvas, x , y):
        Falling_object.__init__(self,canvas,x,y)
        self._img_orange = PhotoImage(file = 'orange(2).gif')
        
    def create(self):
        '''create orange'''
        self._canvas.create_image(self._x,self._y, image = self._img_orange, tag = "orange")
   
    