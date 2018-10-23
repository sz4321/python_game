'''Final project
Winter 2017
author Sebrina Zeleke(stz4)
'''

from tkinter import *
import random
from apple import *
from snail import *
from rat import *
from plate import *
from orange import *

#Dimension of the canvas
canv_dim = 600

class Game:
    '''Creates the GUI for the game'''
    def __init__(self,root):
        '''Initialize the values'''
        self._root = root
        self._canvas = Canvas(root, width = canv_dim , height = canv_dim , bg = 'white')
        self._canvas.pack()
        
        #Create a button for the restart and exit button
        frame = Frame(root)
        frame.pack()
        self.restart = Button(frame, text="Restart" , command = self.restart)
        self.restart.pack(side=LEFT)
        exit1 = Button(frame, text="Exit" , command = quit)
        exit1.pack(side=LEFT )
        
        #Create a label for the instruction
        instruction_label = Label(root, text = 'Only catch the fruits.')
        instruction_label.pack(side = TOP)
        
        instuction_label1 = Label(root,text = 'Use the right arrow key to move to the right and the left arrow key to move to the left.')
        instuction_label1.pack(side = TOP)
        
        #Create a label for score and live
        self.live = StringVar()
        live1 = Label(root, text = 'Lives left:' , bg = 'pink' , font = 30)
        live1.pack(side = LEFT)
        live2 = Label(root, textvariable = self.live ,  bg = 'pink' , font = 30)
        live2.pack(side = LEFT)
        
        #Create a text for game over
        self._score1 = StringVar()
        game_over_1 = Label(root,text = 'Score:' , bg= 'yellow' , font = 50)
        game_over_1.pack(side = TOP )
        game_over_2 = Label(root,textvariable = self._score1 , bg = '#FF8C00' , font = 50)
        game_over_2.pack(side = TOP)
         

        #Handle apple
        self.s_apple = []
        self._canvas.after(40, self.sort_apple)
        
        #Handle orange
        self.s_orange = []
        self._canvas.after(40, self.sort_orange)
       
        #Handle plate
        self.s_snail = []
        self._canvas.after(40, self.sort_snail)

        #handle plate
        self.plate = Plate(self._canvas)
        self.sort_plate()
        self.plate
        
        #Handle rat
        self.s_rat = []
        self._canvas.after(40, self.sort_rat)
        
        #Score
        self._score = 0
        self._score1.set(self._score)
        self._falling = 0
                
#Got the idea of this code from lab 12
    def sort_apple(self):
        '''create and move an apple'''
        if len(self.s_apple)<3:
            self.s_apple.append(Apple(self._canvas , random.randint(10, canv_dim-10),0 , 5))
        self._canvas.delete("apple")
    
        for apple in self.s_apple[:]:
            if self._score > 9:
                apple._vel = 9
            apple.move()
            apple.create()
            #if apple off screen, remove from list
            if apple.get_y() > 600:
                self.s_apple.remove(apple)
                self._falling +=1

            #detect collision   
            if apple.get_x() in range(self.plate.get_x()-50,self.plate.get_x()+50) and apple.get_y() in range(520,540):
                self.s_apple.remove(apple)
                self._score +=1
        
        #if the game if not over call self.sort_apple              
        if not self._falling >= 10: 
            self._canvas.after(40,self.sort_apple)
            self.restart.configure(state = DISABLED)
        else:
            #otherwise print a game over text
            self._canvas.create_text(300 , 300 , text = 'Game Over. Press restart to try again.' , font = 'Times 20 italic' , fill = 'blue')
            self.restart.configure(state = NORMAL)
        #update the self._falling and self._score
        self._score1.set(self._score)
        self.live3 = 10 - self._falling
        self.live.set(self.live3)
        
        
    def sort_orange(self):
        '''create and move an orange'''
        if self._score>4:
            if len(self.s_orange)<2:
                self.s_orange.append(Orange(self._canvas , random.randint(10, canv_dim-10),0))
            self._canvas.delete('orange')
            
        for orange in self.s_orange[:]:
            if self._score >= 15:
                orange._vel = 10
            orange.move()
            orange.create()
        #if orange off screen remove from list
            if orange.get_y() > 600:
                self.s_orange.remove(orange)
                self._falling +=1
        # detect collision       
            if orange.get_x() in range(self.plate.get_x()-50,self.plate.get_x()+50) and orange.get_y() in range(520,540):
                self.s_orange.remove(orange)
                self._score +=1
        if not self._falling >= 10:
            self._canvas.after(40,self.sort_orange)
            
        
            
    def sort_snail(self):
        '''create and move a snail'''
        if self._score >= 2:
            if len(self.s_snail)<3:  
                self.s_snail.append(Snail(self._canvas , random.randint(10, canv_dim-10),0))
            self._canvas.delete('snail')
        
        for snail in self.s_snail[:]:
            if self._score > 9:
                snail._vel = 9
            snail.move()
            snail.create()
            
            #if snail off screen, remove from list
            if snail.get_y() > 600:
                self.s_snail.remove(snail)
            
            #detect collision    
            if snail.get_x() in range(self.plate.get_x()-50,self.plate.get_x()+50) and snail.get_y() in range(520,540):
                self.s_snail.remove(snail)
                self._score -=1
                
        #if game nor over call self.sort_snail       
        if not self._falling >= 10:
            self._canvas.after(40,self.sort_snail)
    def sort_rat(self):
        '''create and move the rat'''
        if self._score >5:
            if len(self.s_rat) < 3:
                self.s_rat.append(Rat(self._canvas , random.randint(10, canv_dim-10),0))
        self._canvas.delete('rat')
            
        for rat in self.s_rat[:]:
            if self._score > 13:
                rat._vel = 9
            rat.move()
            rat.create()
        
            #if rat is off screen, remover from list
            if rat.get_y() > 600:
                self.s_rat.remove(rat)
            
            #detect collision
            if rat.get_x() in range(self.plate.get_x()-50,self.plate.get_x()+50) and rat.get_y() in range(520,540):
                    self.s_rat.remove(rat)
                    self._score -=1
        if not self._falling >= 10:       
            self._canvas.after(40, self.sort_rat)    
        
    
    
    def sort_plate(self):
        '''create and move rat'''
        self.plate.create() 
        
    def restart(self):
        self._canvas.delete(ALL)
        self.s_apple = []
        self._canvas.after(40, self.sort_apple)
        
        #handle orange
        self.s_orange = []
        self._canvas.after(40, self.sort_orange)
        
        #handle plate
        self.s_snail = []
        self._canvas.after(40, self.sort_snail)

        #handle plate
        self.plate = Plate(self._canvas)
        self.sort_plate()
        self.plate
        
        #handle rat
        self.s_rat = []
        self._canvas.after(40, self.sort_rat)
        
        #score
        self._score = 0
        self._falling = 0
 
        
        
        
root = Tk()
root.title("Catch the falling fruits")
Game(root)
root.mainloop()


        
