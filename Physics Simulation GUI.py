# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 12:33:36 2020

@author: gunda
"""

import sys
import os
from tkinter import *
import tkinter as tk
from tkinter import ttk

class PhysicsSimUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Riley's Physics Simulation UI")
        self.geometry("600x300")
        
        # labels
        self.intro_label = Label(self, text = "Welcome to Riley's Physics Simulation UI",
                                 fg = 'blue', relief = RIDGE, borderwidth = 3)
        self.intro_label.config(font = ('Courier',15,'bold'))
        self.intro_label.place(x = 25, y = 5)
        
        # buttons
        self.exe_button1 = Button(self, text = "Charged Particle Moving in Magnetic Field", fg = "black",
                                  command = self.ChargedParticleMovedInMagneticField())
        self.exe_button1.config(font=('Times', 12, 'bold'))
        self.exe_button1.place(x = 25, y = 40)
        
        self.exe_button2 = Button(self, text = "Planetary Motion", fg = "black",
                                  command = self.PlanetaryMotion())
        self.exe_button2.config(font=('Times', 12, 'bold'))
        self.exe_button2.place(x = 25, y = 75)
        
        self.exe_button3 = Button(self, text = "Simple Harmonic Motion", fg = "black",
                                  command = self.SimpleHarmonicMotion())
        self.exe_button3.config(font=('Times', 12, 'bold'))
        self.exe_button3.place(x = 25, y = 110)
        
        self.exe_button4 = Button(self, text = "Friction Between Two Piled Blocks", fg = "black",
                                 command = self.FrictionBetweenTwoPiledBlocks())
        self.exe_button4.config(font=('Times', 12, 'bold'))
        self.exe_button4.place(x = 25, y = 145)
    
    def ChargedParticleMovedInMagneticField(self):
        print("Charged_Particle_Moving_In_Magnetic_Field.py is executed")
    
    def PlanetaryMotion(self):
        print("Planetary_Motion.py is executed")
    
    def SimpleHarmonicMotion(self):
        print("Simple_Harmonic_Motion.py is executed")
    
    def FrictionBetweenTwoPiledBlocks(self):
        #os.system('Friction_Between_Two_Piled_Blocks.py')
        print("Friction_Between_Two_Piled_Blocks.py is executed")
        
if __name__ == '__main__':
    
    PhysicsSimUI()
    mainloop()