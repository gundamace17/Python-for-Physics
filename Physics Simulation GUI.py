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
import webbrowser

class PhysicsSimUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Riley's Physics Simulation UI")
        self.geometry("1500x700")
        
        # labels
        self.intro_label = Label(self, text = "Welcome to Riley's Physics Simulation UI",
                                 fg = 'blue', relief = RIDGE, borderwidth = 3)
        self.intro_label.config(font = ('Courier',15,'bold'))
        self.intro_label.place(x = 25, y = 5)
        
        # buttons for simulations
        self.exe_button1 = Button(self, text = "Charged Particle Moving in Magnetic Field", fg = "black",
                                  bg = 'grey', command = self.ChargedParticleMovedInMagneticField)
        self.exe_button1.config(font=('Oswald', 12, 'bold'), width = 40)
        self.exe_button1.place(x = 25, y = 90)
        
        self.exe_button2 = Button(self, text = "Planetary Motion", fg = "black",
                                  bg = 'grey', command = self.PlanetaryMotion)
        self.exe_button2.config(font=('Oswald', 12, 'bold'), width = 40)
        self.exe_button2.place(x = 25, y = 130)
        
        self.exe_button3 = Button(self, text = "Simple Harmonic Motion", fg = "black",
                                  bg = 'grey', command = self.SimpleHarmonicMotion)
        self.exe_button3.config(font=('Oswald', 12, 'bold'), width = 40)
        self.exe_button3.place(x = 25, y = 170)
        
        self.exe_button4 = Button(self, text = "Friction Between Two Piled Blocks", fg = "black",
                                  bg = 'grey', command = self.FrictionBetweenTwoPiledBlocks)
        self.exe_button4.config(font=('Oswald', 12, 'bold'), width = 40)
        self.exe_button4.place(x = 25, y = 210)
        
        # button for closing the app
        self.exe_button5 = Button(self, text = "Exit", fg = "black",
                                  bg = 'grey', command = self.destroy)
        self.exe_button5.config(font=('Itim', 12, 'bold'), width = 12)
        self.exe_button5.place(x = 1150, y = 650)
        
        # button for going to the source code
        self.exe_button5 = Button(self, text = "Source Code", fg = "black",
                                  bg = 'grey', command = self.sourceCode)
        self.exe_button5.config(font=('Itim', 12, 'bold'), width = 12)
        self.exe_button5.place(x = 1300, y = 650)
    
    def ChargedParticleMovedInMagneticField(self):
        os.system('Charged_Particle_Moving_In_Magnetic_Field.py')
        print("Charged_Particle_Moving_In_Magnetic_Field.py is executed")
    
    def PlanetaryMotion(self):
        os.system('Planetary_Motion.py')
        print("Planetary_Motion.py is executed")
    
    def SimpleHarmonicMotion(self):
        os.system('Simple_Harmonic_Motion.py')
        print("Simple_Harmonic_Motion.py is executed")
    
    def FrictionBetweenTwoPiledBlocks(self):
        os.system('Friction_Between_Two_Piled_Blocks.py')
        print("Friction_Between_Two_Piled_Blocks.py is executed")
        
    def sourceCode(self):
        webbrowser.open(url, new = 1)
        
if __name__ == '__main__':
    
    url = 'https://github.com/gundamace17/Python-for-Physics'
    
    PhysicsSimUI()
    mainloop()