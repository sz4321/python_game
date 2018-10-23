'''Final project
Winter 2017
author Sebrina Zeleke(stz4)
'''

from tkinter import *
from falling_from_the_top import *

class Rat(Falling_object):
    '''initializes values'''
    def __init__(self,canvas, x , y):
        Falling_object.__init__(self,canvas,x,y)
        self._img_rat = PhotoImage(file = 'rat3(1).gif')
        
    def create(self):
        '''create a rat'''
        self._canvas.create_image(self._x,self._y, image = self._img_rat, tag = "rat")
   
    