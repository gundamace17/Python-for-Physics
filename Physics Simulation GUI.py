# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 12:33:36 2020

@author: Riley Lien
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
        # Set the English version the default
        self.EnglishVer()

        # radiobuttons for selecting languages
        self.v = tk.IntVar()
        self.v.set(1)
        self.xr = 5
        self.lang = [('English', 1), ('繁體中文', 2)]

        tk.Radiobutton(self.label_frameLan, text=self.lang[0][0], variable=self.v,
                       value = self.lang[0][1], bg = 'lightgrey', padx = 20, font = ('Times', 14, 'bold'),
                       activebackground = 'lightgrey', command=self.EnglishVer).place(x = self.xr, y = 5)

        tk.Radiobutton(self.label_frameLan, text=self.lang[1][0], variable=self.v,
                       value=self.lang[1][1], bg='lightgrey', padx=20, font=('Times', 14, 'bold'),
                       activebackground='lightgrey', command=self.MandarinVer).place(x=self.xr+150, y=5)

    # function for displaying English version
    def EnglishVer(self):
        self.title("Riley's Physics Simulation GUI")
        self.geometry("1300x700")
        self.config(bg='lightgrey')

        # labels
        self.intro_label = Label(self, text="Welcome to Riley's Physics Simulation UI",
                                 fg='blue', relief=RIDGE, borderwidth=3, width=102)
        self.intro_label.config(font=('Courier', 15, 'bold'))
        self.intro_label.place(x=35, y=5)

        self.v2 = StringVar()
        self.v2.set("Riley Lien, PoUgly Chen")
        self.vinfo = Message(self, textvariable=self.v2, bg='sandy brown', relief=GROOVE,
                             font=('Verdana', 16, 'bold'), width=1800).place(x=35, y=650)

        # button for closing the app
        self.exe_button5 = Button(self, text="Exit", fg="black",
                                  bg='grey', command=self.destroy)
        self.exe_button5.config(font=('Itim', 12, 'bold'), width=12)
        self.exe_button5.place(x=950, y=650)

        # button for going to the source code
        self.exe_button5 = Button(self, text="Source Code", fg="black",
                                  bg='grey', command=self.sourceCode)
        self.exe_button5.config(font=('Itim', 12, 'bold'), width=12)
        self.exe_button5.place(x=1100, y=650)

        # labelframes for selecting languages
        self.label_frameLan = LabelFrame(height=75, width=450, bg="lightgrey", bd="3", colormap="new",
                                         relief="groove", text="Languages")
        self.label_frameLan.config(font=('Courier', 18, 'bold'))
        self.label_frameLan.place(x=35, y=45)

        self.label_frame1 = LabelFrame(height = 500, width = 450, bg = "lightgrey", bd = "3", colormap = "new",
                                       relief = "groove", text = "Topics")
        self.label_frame1.config(font = ('Courier', 20, 'bold'))
        self.label_frame1.place(x = 35, y = 125)

        # buttons for simulations
        self.exe_button1 = Button(self.label_frame1, text = "Charged Particle Moving in Magnetic Field", fg = "black",
                                  bg = 'tomato', command = self.ChargedParticleMovedInMagneticField)
        self.exe_button1.config(font=('Oswald', 12, 'bold'), width = 40)
        self.exe_button1.place(x = 15, y = 10)

        self.exe_button2 = Button(self.label_frame1, text="Planetary Motion", fg="black",
                                  bg='plum1', command=self.PlanetaryMotion)
        self.exe_button2.config(font=('Oswald', 12, 'bold'), width = 40)
        self.exe_button2.place(x = 15, y = 50)

        self.exe_button3 = Button(self.label_frame1, text="Simple Harmonic Motion", fg="black",
                                  bg='skyblue1', command=self.SimpleHarmonicMotion)
        self.exe_button3.config(font=('Oswald', 12, 'bold'), width = 40)
        self.exe_button3.place(x = 15, y = 90)

        self.exe_button4 = Button(self.label_frame1, text="Friction Between Two Piled Blocks", fg="black",
                                  bg='mediumpurple1', command=self.FrictionBetweenTwoPiledBlocks)
        self.exe_button4.config(font=('Oswald', 12, 'bold'), width=40)
        self.exe_button4.place(x=15, y=130)

        self.exe_button4 = Button(self.label_frame1, text="One Dimensional Collision", fg="black",
                                  bg='gold', command=self.OneDimensionCollision)
        self.exe_button4.config(font=('Oswald', 12, 'bold'), width=40)
        self.exe_button4.place(x=15, y=170)

        self.v = tk.IntVar()
        self.v.set(1)
        self.xr = 5
        self.lang = [('English', 1), ('繁體中文', 2)]

        tk.Radiobutton(self.label_frameLan, text=self.lang[0][0], variable=self.v,
                       value=self.lang[0][1], bg='lightgrey', padx=20, font=('Times', 14, 'bold'),
                       activebackground='lightgrey', command=self.EnglishVer).place(x=self.xr, y=5)

        tk.Radiobutton(self.label_frameLan, text=self.lang[1][0], variable=self.v,
                       value=self.lang[1][1], bg='lightgrey', padx=20, font=('Times', 14, 'bold'),
                       activebackground='lightgrey', command=self.MandarinVer).place(x=self.xr + 150, y=5)

    # Version for displaying Mandarin version
    def MandarinVer(self):
        self.title("Riley 物理模擬使用者介面")
        self.geometry("1300x700")
        self.config(bg='lightgrey')

        # labels
        self.intro_label = Label(self, text="歡迎使用 Riley 物理模擬軟體",
                                 fg='blue', relief=RIDGE, borderwidth=3, width=102)
        self.intro_label.config(font=('Courier', 15, 'bold'))
        self.intro_label.place(x=35, y=5)

        self.v2 = StringVar()
        self.v2.set("Riley Lien, PoUgly Chen")
        self.vinfo = Message(self, textvariable=self.v2, bg='sandy brown', relief=GROOVE,
                             font=('Verdana', 16, 'bold'), width=1800).place(x=35, y=650)

        # button for closing the app
        self.exe_button5 = Button(self, text="關閉程式", fg="black",
                                  bg='grey', command=self.destroy)
        self.exe_button5.config(font=('Itim', 12, 'bold'), width=12)
        self.exe_button5.place(x=950, y=650)

        # button for going to the source code
        self.exe_button5 = Button(self, text="前往原始碼", fg="black",
                                  bg='grey', command=self.sourceCode)
        self.exe_button5.config(font=('Itim', 12, 'bold'), width=12)
        self.exe_button5.place(x=1100, y=650)

        # labelframes for selecting languages
        self.label_frameLan = LabelFrame(height=75, width=450, bg="lightgrey", bd="3", colormap="new",
                                         relief="groove", text="選擇語言")
        self.label_frameLan.config(font=('Courier', 18, 'bold'))
        self.label_frameLan.place(x=35, y=45)

        self.label_frame1 = LabelFrame(height=500, width=450, bg="lightgrey", bd="3", colormap="new",
                                       relief="groove", text="選擇主題")
        self.label_frame1.config(font=('Courier', 20, 'bold'))
        self.label_frame1.place(x=35, y=125)

        # buttons for simulations
        self.exe_button1 = Button(self.label_frame1, text="帶電粒子在磁場中運動", fg="black",
                                  bg='tomato', command=self.ChargedParticleMovedInMagneticField)
        self.exe_button1.config(font=('Oswald', 12, 'bold'), width=40)
        self.exe_button1.place(x=15, y=10)

        self.exe_button2 = Button(self.label_frame1, text="行星運動", fg="black",
                                  bg='plum1', command=self.PlanetaryMotion)
        self.exe_button2.config(font=('Oswald', 12, 'bold'), width=40)
        self.exe_button2.place(x=15, y=50)

        self.exe_button3 = Button(self.label_frame1, text="簡協運動", fg="black",
                                  bg='skyblue1', command=self.SimpleHarmonicMotion)
        self.exe_button3.config(font=('Oswald', 12, 'bold'), width=40)
        self.exe_button3.place(x=15, y=90)

        self.exe_button4 = Button(self.label_frame1, text="相堆疊木塊間的摩擦力", fg="black",
                                  bg='mediumpurple1', command=self.FrictionBetweenTwoPiledBlocks)
        self.exe_button4.config(font=('Oswald', 12, 'bold'), width=40)
        self.exe_button4.place(x=15, y=130)

        self.exe_button4 = Button(self.label_frame1, text="一維彈性碰撞", fg="black",
                                  bg='gold', command=self.OneDimensionCollision)
        self.exe_button4.config(font=('Oswald', 12, 'bold'), width=40)
        self.exe_button4.place(x=15, y=170)

        # self.v = tk.IntVar()
        self.v.set(2)
        # self.xr = 5
        # self.lang = [('English', 1), ('繁體中文', 2)]

        tk.Radiobutton(self.label_frameLan, text=self.lang[0][0], variable=self.v,
                       value=self.lang[0][1], bg='lightgrey', padx=20, font=('Times', 14, 'bold'),
                       activebackground='lightgrey', command=self.EnglishVer).place(x=self.xr, y=5)

        tk.Radiobutton(self.label_frameLan, text=self.lang[1][0], variable=self.v,
                       value=self.lang[1][1], bg='lightgrey', padx=20, font=('Times', 14, 'bold'),
                       activebackground='lightgrey', command=self.MandarinVer).place(x=self.xr + 150, y=5)
    
    def ChargedParticleMovedInMagneticField(self):
        os.system('python Charged_Particle_Moving_In_Magnetic_Field.py')
        print("Charged_Particle_Moving_In_Magnetic_Field.py is executed")
    
    def PlanetaryMotion(self):
        os.system('python Planetary_Motion.py')
        print("Planetary_Motion.py is executed")
    
    def SimpleHarmonicMotion(self):
        os.system('python Simple_Harmonic_Motion.py')
        print("Simple_Harmonic_Motion.py is executed")
    
    def FrictionBetweenTwoPiledBlocks(self):
        os.system('python Friction_Between_Two_Piled_Blocks.py')
        print("Friction_Between_Two_Piled_Blocks.py is executed")

    def OneDimensionCollision(self):
        os.system('python One_Dimension_Collision.py')
        print("One_Dimension_Collision.py is executed")
        
    def sourceCode(self):
        webbrowser.open(url, new = 1)
        
if __name__ == '__main__':
    
    url = 'https://github.com/gundamace17/Python-for-Physics'
    
    PhysicsSimUI()
    mainloop()