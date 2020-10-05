# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 17:51:17 2020

@author: gunda
"""

from vpython import *

size, m, q = 0.005, 1E-10, 1E-9 # the radius, mass and charges of the particle
theta = radians(int(input('Angle between the initial velocity and xy-plane? '))) # the angle between initial velocity and xy-plane
phi = radians(int(input('Angle bwtween the projection of the initial velocity on xy-plane and the x-axis? '))) # the angle bwtween the projection of the initial velocity on xy-plane and the x-axis
v0 = 10*vec(cos(theta)*cos(phi), cos(theta)*sin(phi), sin(theta))  # initial velocity of the particle
L = 0.4                      # length of axes
B_field = vec(10, 0, 0)      # magnetic field
t, dt = 0, 1E-5              # time, time intervals

#scene = canvas(title="Charged Particle in Magnetic Field", width=800, height=600, x=0, y=0, 
#               center=vec(0, 0, 0), range=0.6*L, background=color.black)
scene2 = display(title = "Charged Particle in Magnetic Field", width = 800, height = 600,
                 center=vec(0, 0, 0), range=0.6*L, background=color.black, visible = 1, fullscreen = 1)
if(theta == pi/2 or phi == pi/2):
    scene.camera.pos = vec(L, L/4, L/4)
    scene.camera.axis = vec(-L, -L/4, -L/4)
else:
    scene.camera.pos = vec(L/4, L/4, L)
    scene.camera.axis = vec(-L/4, -L/4, -L)
    
# Create a particle with charge
charge = sphere(pos=vec(0, 0, 0), radius=2*size, v=v0, color=color.red, m=m,
                make_trail=True, retain = 1000)
if q > 0:
    label_charge = label(text = '+', font = 'sans', xoffset = 20, yoffset = 20)
elif q < 0:
    label_charge = label(text = '-', font = 'sans', xoffset = 20, yoffset = 20)
else:
    label_charge = label(text = 'N', font = 'sans', xoffset = 20, yoffset = 20)

# building of coordinate and labels
arrow_x = arrow(pos=vec(-L/2, 0, 0), axis=vec(L, 0, 0), shaftwidth=0.6*size,
                color=color.yellow)
label_x = label(pos=vec(L/2, 0, 0), text="x", xoffset=25, color=color.yellow,
                font="sans")
arrow_y = arrow(pos=vec(0, -L/2, 0), axis=vec(0, L, 0), shaftwidth=0.6*size,
                color=color.yellow)
label_y = label(pos=vec(0, L/2, 0), text="y", yoffset=25, color=color.yellow,
                font="sans")
arrow_z = arrow(pos=vec(0, 0, -L/2), axis=vec(0, 0, L), shaftwidth=0.6*size,
                color=color.yellow)
label_z = label(pos=vec(0, 0, L/2), text="z", xoffset=-25, yoffset=-25,
                color=color.yellow, font="sans")

# arrow tag for labeling the magnetic field
B_vectors_px = [vec(-L/2, L/10, L/10), vec(-L/2, L/2, 0), vec(-L/2, -L/2, 0),
                vec(-L/2, 0, L/2), vec(-L/2, 0, -L/2)]
B_vectors_nx = [vec(L/2, L/10, L/10), vec(L/2, L/2, 0), vec(L/2, -L/2, 0),
                vec(L/2, 0, L/2), vec(L/2, 0, -L/2)]
if diff_angle(B_field, arrow_x.axis) == radians(0):
    for i in range(len(B_vectors_px)):
        arrow_B = arrow(pos = B_vectors_px[i], axis = B_field.norm()*0.4,
                          shaftwidth = size*0.5, color = color.green)
elif diff_angle(B_field, arrow_x.axis) == radians(180):
    for i in range(len(B_vectors_nx)):
        arrow_B = arrow(pos = B_vectors_nx[i], axis = B_field.norm()*0.4,
                          shaftwidth = size*0.5, color = color.green)

label_B = label(pos=vec(-L/2, L/10, L/10), text="B", xoffset=25, yoffset=25,
                color=color.green, font="sans")

# arrow for labeling the velocity and acceleration
arrow_v = arrow(pos=charge.pos, shaftwidth=0.5*size, color=color.blue)
arrow_a = arrow(pos=charge.pos, shaftwidth=0.5*size, color=color.magenta)
label_v = label(pos=charge.pos, text = 'v', xoffset = 15, yoffset = 15,
                color = color.blue, font = 'sans')
label_a = label(pos=charge.pos, text = 'a', xoffset = -15, yoffset = -15,
                color = color.magenta, font = 'sans')

while(abs(charge.pos.x) < 0.6*L and abs(charge.pos.y) < 0.6*L and
      abs(charge.pos.z) < 0.6*L):
    rate(500)
# calculate the composition of forces and update the acceleration, velocity and position
    F = q*cross(charge.v, B_field)
    charge.a = F/charge.m
    charge.v += charge.a*dt
    charge.pos += charge.v*dt
# update the arrow and label for velocity and acceleration
    arrow_v.pos = charge.pos
    arrow_a.pos = charge.pos
    label_charge.pos = charge.pos
    label_v.pos = arrow_v.pos + arrow_v.axis
    label_a.pos = arrow_a.pos + arrow_a.axis
    arrow_v.axis = charge.v.norm()*0.1
    arrow_a.axis = charge.a.norm()*0.1
# time update
    t += dt