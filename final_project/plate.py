from tkinter import *
canv_dim = 600
'''Final project
Winter 2017
author Sebrina Zeleke(stz4)
'''

class Plate:
    '''Create a bowl at the bottom of the screen'''
    def __init__(self, canvas ,  x= 300 , y = 560):
        '''initializes values'''
        self._x = x
        self._canvas = canvas
        self._y = y
        self._vel = 50
        self._bowl = PhotoImage(file = 'bowl(2).gif')
        self._canvas.bind('<Right>' , self.move_right)
        self._canvas.bind('<Left>' , self.move_left)
        self._canvas.focus_set()
       
    def move_right(self,event):
        '''move the bowl to the right'''
        if self._x> canv_dim-50:
            self._x = 550
        self._canvas.delete('plate')
        self._canvas.create_image(self._x+self._vel,self._y,image = self._bowl, tag = 'plate')
        self._x +=self._vel

    def move_left(self,event):
        '''move the bowl to the left'''
        if self._x < 50:
            self._x = 50
        self._canvas.delete('plate')
        self._canvas.create_image(self._x-self._vel,self._y,image = self._bowl, tag = 'plate')
        self._x -= self._vel
        
    def create(self):
        '''create a bowl'''
        self._canvas.create_image(self._x,self._y,image = self._bowl, tag = 'plate')
        
    def get_x(self):
        '''Accessor for x'''
        return self._x
            
    def get_y(self):
        '''Accessor for y'''
        return self._y
