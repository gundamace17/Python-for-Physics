# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 12:31:30 2020

@author: gunda
"""

from vpython import *

"""
 1. Setting for Parameters, variables and Initial values
"""
d1 , h1, w1 = 1.8, 0.2, 0.2        # bottom block1: L = 1.8m, H = 0.2m, W = 0.2 m
d2 , h2, w2 = 0.2, 0.2, 0.2        # upper block2: L = 0.2m, H = 0.2m, W = 0.2 m
m1, v1, c1 = 0.2, 0.0, color.red   # bottom block1: mass = 0.2 kg, initial velocity = 0.0 m/s
m2, v2, c2 = 0.1, 5.0, color.green # upper block2: mass = 0.1 kg, initial velocity = 2.0 m/s
xmax, xmin = 2.0, -2.0             # the range of x-axis
g = 9.8                            # acceleration of gravity = 9.8 m/s^2
mu = 0.6                           # coefficient of kinetic friction
dt = 0.0005     	               # frame rate of the screen, unit is second(s)
t = 0         	                   # time the simulation takes. the unit is second(s), initial value is 0.
bx = 0      	                   # variable for storing the initial position of b2
i, te = 0, -1                      # variables for storing the time interval that b1 and b2 take to reach the final velocity

"""
 2. Screen Setting
"""
# Create the window for animation
scene = canvas(title = "Two Piled Blocks", width = 800, height = 300,
               center = vec(0, 0.4, 0), background = vec(0, 0.6, 0.6))

# Create the floor where two blocks slide
floor = box(pos = vec(0, -0.5 * h2, 0), size = vec(xmax - xmin, 0.05, 0.8),
            texture = textures.metal)

# Create the bottom block b1 which is at the most left position, xmin + d1/2,
# with initial velocity v1
b1 = box(pos = vec(xmin + d1/2, 0, 0), size = vec(d1, h1, w1),
         texture = "Wood.jpg", v = vec(v1, 0, 0))

# Create the upper block b2.
# In order not to let b2 slides out of b1:
# If v2 >= v1, set the position of b2 at xmin + d2*0.5.
# If v2 < v1, set the position of b2 at xmin + d1 - d2*0.5.
if(v2 >= v1): bx = xmin + 0.5*d2
else: bx = xmin + d1 - 0.5*d2
b2 = box(pos = vec(bx, h1, 0), size = vec(d2, h2, w2), texture = textures.wood,
         v = vec(v2, 0, 0))

# Graphs plotting
gd = graph(title="<i>E</i> - <i>t</i> plot", x=0, y=300, width=600, height=450, xtitle="<i>t</i> (s)",
           ytitle="red: <i>K</i><sub>1</sub>, green: <i>K</i><sub>2</sub>, blue: <i>E</i> (J)")
kt1 = gcurve(graph=gd, color=c1)
kt2 = gcurve(graph=gd, color=c2)
et = gcurve(graph=gd, color=color.blue)
gd2 = graph(title="<i>v</i> - <i>t</i> plot", x=0, y=750, width=600, height=450, xtitle="<i>t</i> (s)",
            ytitle="red: <i>v</i><sub>1</sub>, green: <i>v</i><sub>2</sub> (m/s)")
vt1 = gcurve(graph=gd2, color=c1)
vt2 = gcurve(graph=gd2, color=c2)

"""
 3. Display the motion of blocks until b1 reaches the edge of the floor or
    b2 reaches the edge of b1
"""
while((b1.pos.x <= xmax - d1/2) and (b2.pos.x + d2/2 <= b1.pos.x + d1/2 + 0.001)):
# Frame rate
    rate(500)
# Determine the kinetic friction and the direction of acceleration
# by the velocity of b1 and b2 
    if(b2.v.x > b1.v.x):
        force = mu * m2 * g
        b1.a = vec(force / m1, 0, 0)
        b2.a = vec(-force / m2, 0, 0)
    elif(b2.v.x < b1.v.x):
        force = mu * m2 * g
        b1.a = vec(-force / m1, 0, 0)
        b2.a = vec(force / m2, 0, 0)
    else:
        force = 0
        b1.a = vec(0, 0, 0)
        b2.a = vec(0, 0, 0)

# Storing the time of b1 and b2 that they reach the same velocity
    if(abs(b2.v.x - b1.v.x) < 0.0005 and i == 0):
        te = t
        i = 1     

# Calculate the velocity and position of b1 and b2
    b1.v += b1.a * dt
    b2.v += b2.a * dt
    b1.pos += b1.v * dt
    b2.pos += b2.v * dt

# Calculate the kinetic energy and mechanical energy of the system.
# Plotting the E-t graph
    k1 = 0.5 * m1 * mag2(b1.v)
    k2 = 0.5 * m2 * mag2(b2.v)
    e = k1 + k2
    kt1.plot(pos = (t, k1))            
    kt2.plot(pos = (t, k2))
    et.plot(pos = (t, e))

# Plotting the v-t graphs for v1 and v2
    vt1.plot(pos = (t, b1.v.x))            
    vt2.plot(pos = (t, b2.v.x))

# Update time parameter
    t += dt

# while loop ends. print out the final velocity and the time
# b1 and b2 take to reach the final velocity
print("v1 = ", b1.v.x)
print("v2 = ", b2.v.x)
print("te = ", te)
print("end")