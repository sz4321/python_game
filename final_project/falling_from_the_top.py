'''Final project
Winter 2017
author Sebrina Zeleke(stz4)
'''

from tkinter import *
canv_dim = 600

class Falling_object:
    def __init__(self,canvas, x , y):
        '''initialize values'''
        self._canvas = canvas
        self._x = x
        self._y = y
        self._vel = 5
     
    def move(self):
        '''move the apple'''
        self._y += self._vel
    
    def get_y(self):
        '''accessor for y'''
        return self._y
    
    def get_x(self):
        '''accessor for x'''
        return self._x

    def off_screen(self):
        '''off screen'''
        return self.get_x > canv_dim
