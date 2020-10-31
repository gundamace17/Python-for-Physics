# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 19:42:55 2020

@author: gunda
"""

from vpython import *

"""
Simple Harmonic Motion
 1. Initialize the parameters
"""
m = 4               # mass of the block: 4 kg
size = 1            # side length of the block: 1 m
R = 5               # amplitude of the SHM: 5 m
k = 1               # elastic constant: 1 N/m
L0 = R + size       # original length of the spring
i = 0               # times that the block pass by the origin
t = 0               # time
dt = 0.001          # time interval

"""
 2. Screen setting
"""
# Create the window, floor, block and spring
scene = canvas(title = "Simple Harmonic Motion", width = 800, height = 400,
               x = 0, y = 0, background = vec(0, 0.6, 0.6))
floor = box(pos = vec(0, -(size+0.1)/2, 0), size = vec(2*L0, 0.1, R),
            texture = textures.metal)
wall = box(pos = vec(-L0, 0, 0), size = vec(0.1, size, R), texture = textures.metal)
block = box(pos = vec(R+size/2, 0, 0), size = vec(size, size, size),
            texture = textures.wood, v = vec(0, 0, 0))
spring = helix(pos = vec(-L0, 0, 0), radius = 0.3*size, thickness = 0.05*size,
               color = color.yellow)
spring.axis = block.pos - spring.pos - vec(size/2, 0, 0)

# Setting the angle of the camera
scene.camera.pos = vec(5, 3, 5)
scene.camera.axis = vec(-5, -3, -5)

# Create the arrow and label for velocity and acceleration
arrow_v = arrow(pos = block.pos + vec(0, size, 0), axis = vec(0, 0, 0),
                shaftwidth = 0.3*size, color = color.green)
label_v = label(pos = arrow_v.pos, text = 'v', xoffset = -30, yoffset = 20 )
arrow_a = arrow(pos = block.pos + vec(0, 2*size, 0), axis = vec(0, 0, 0),
                shaftwidth = 0.3*size, color = color.magenta)
label_a = label(pos = arrow_a.pos, text = 'a', xoffset = 30, yoffset = 20 )

# Figure plotting of displacement, velocity and acceleration to the time
gd = graph(title = "plot", width = 600, height = 450, x = 0, y = 400, xtitle = "<i>t</i>(s)", 
           ytitle = "blue: <i>x</i>(m), green: <i>v</i>(m/s), magenta: <i>a</i>(m/s<sup>2</sup>)")
xt = gcurve(graph = gd, color = color.blue)
vt = gcurve(graph = gd, color = color.green)
at = gcurve(graph = gd, color = color.magenta)

"""
 3. Setting the period of the motion
"""
while(i < 3):
    rate(1000)
# Calculate the length, deformation and restoring force
    spring.axis = block.pos - spring.pos - vec(0.5*size, 0, 0)
    F = -k * (spring.axis - vec(L0, 0, 0))
    
# Calculate the acceleration of the block and update the velocity and position
    block.a = F/m
    block.v += block.a*dt
    block.pos += block.v*dt
    
# Update the position, direction and length of velocity and acceleration arrows
    arrow_v.pos = block.pos + vec(0, size, 0)
    arrow_a.pos = block.pos + vec(0, 2*size, 0)
    arrow_v.axis = block.v
    arrow_a.axis = block.a
    
    label_v.pos = arrow_v.pos
    label_a.pos = arrow_a.pos
    
# Plotting x-t, v-t and a-t schematics
    xt.plot(pos = (t, block.pos.x - size/2))
    vt.plot(pos = (t, block.v.x))
    at.plot(pos = (t, block.a.x))
    
# Determine if the block is back to the origin and count the times block passes by the origin
    if(block.pos.x > R + size/2 and block.v.x > 0):
        print(i, t)
        i += 1
        
# Time parasmeter update
    t += dt
