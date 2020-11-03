# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 21:48:48 2020

@author: Riley Lien
"""
from vpython import *

"""
 1. Setting for Parameters, Variables and Initial Values
"""
d1, m1, v1, c1 = 0.2, 0.5, 1.0, color.red         # width of block 1 = 0.2 m, mass = 0.5 kg, initial velocity = 0.1 m/s, red
d2, m2, v2, c2 = 0.2, 1.0, 0.0, color.green       # width of block 1 = 0.2 m, mass = 0.1 kg, initial velocity = 0.0 m/s, green
L0, k = 0.5, 20.0                                  # The original length of the spring = 0.5 m, elastic constant = 2.0 N/m
xmax, xmin = 2.0, -2.0                            # the range of the x axis
t, dt = 0, 0.0005                                 # time, frame rate. the unit is second (s)

"""
 2. Setting for the Screen
"""
# Create the window of the animation
scene = canvas(title="1 Dimension Collision", width=800, height=300, center=vec(0, 0.4, 0),
               background=vec(0, 0.6, 0.6))

# Create the floor
floor = box(pos=vec(0, -d1/2.0, 0), size=vec((xmax - xmin), 0.05, 0.8), color=color.blue)

# Create the block b1 and b2; set the initial velocity
b1 = box(pos=vec(-L0 - 1, 0, 0), size=vec(d1, d1, d1), color=c1, texture=textures.wood, m=m1, v=vec(v1, 0, 0))
b2 = box(pos=vec(0, 0, 0), size=vec(d2, d2, d2), color=c2, texture=textures.wood, m=m2, v=vec(v2, 0, 0))

# Create the spring, starting point is (-0.5*d2, 0, 0), direction is (-L0, 0, 0)
spring = helix(pos=b2.pos + vec(-0.5*d2, 0, 0), axis=vec(-L0, 0, 0), radius=0.05, thickness=0.03)

# Graphics plotting
gd1 = graph(title="<i>E</i>-<i>t</i> plot", x=0, y=300, width=600, height=450, xtitle="<i>t</i> (s)", 
            ytitle="red: <i>K</i><sub>1</sub>, green: <i>K</i><sub>2</sub>, orange: <i>U</i>, blue: <i>E</i> (J)")
kt1 = gcurve(graph=gd1, color=c1)
kt2 = gcurve(graph=gd1, color=c2)
ut = gcurve(graph=gd1, color=color.orange)
et = gcurve(graph=gd1, color=color.blue)
gd2 = graph(title="<i>v</i>-<i>t</i> and <i>a</i>-<i>t</i> plot", x=0, y=750, width=600, height=450,
            xtitle="<i>t</i> (s)", ytitle="red: <i>v</i><sub>1</sub>, green: <i>v</i><sub>2</sub> (m/s); orange: <i>a</i><sub>1</sub>, blue: <i>a</i><sub>2</sub> (m/s<sup>2</sup>)")
vt1 = gcurve(graph=gd2, color=c1)
vt2 = gcurve(graph=gd2, color=c2)
at1 = gcurve(graph=gd2, color=color.orange)
at2 = gcurve(graph=gd2, color=color.blue)

"""
 3. For the motion of objects, use while loop and stop until one of the block reach the edge of the floor.
    Calculate the restoring force of the spring by Hooke's law: F = -k * Δx
    In order to make the force vector, it needs to be multiplied by the unit vector of spring.axis
    mag(a) = a.mag -> calculate the magnitude of a
    a / mag(a) = a.norm() -> return the unit vector of a
"""
# print out the velocity before the blocks make collision
print("m1=", b1.m, "m2 =", b2.m)
print(b1.v.x, b2.v.x)

while ((b2.pos.x <= xmax - d2/2) and (b1.pos.x >= xmin + d1/2)):
    rate(1000)

# Calculate the distance between two blocks and refresh the starting point of the spring
    dx = b2.pos.x - b1.pos.x - 0.5*d1 - 0.5*d2
    spring.pos = b2.pos + vec(-0.5*d2, 0, 0)

# If the distance between blocks is greater than the original length of the spring,
# the spring is not compressed. The restoring force = 0; the acceleration = 0.
# If the distance between blocks is less than the original length of the spring,
# the spring is compressed. Calculate the restoring force and the acceleration of blocks
    if(dx >= L0):
        spring.axis = vec(-L0, 0, 0)
        dL = 0
        b1.a = vec(0, 0, 0)
        b2.a = vec(0, 0, 0)
    else:
        spring.axis = vec(-dx, 0, 0)
        dL = L0 - dx
        force = vec(-k*dL, 0, 0)
        b1.a = force/b1.m
        b2.a = -force/b2.m

# Update the velocity and position of b1 and b2
    b1.v += b1.a * dt
    b2.v += b2.a * dt
    b1.pos += b1.v * dt
    b2.pos += b2.v * dt

# Calculate the kinetic energy of blocks, elastic potential and mechanical energy of the system; plotting the graphics
    k1 = 0.5 * m1 * b1.v.mag2
    k2 = 0.5 * m2 * b2.v.mag2
    u = 0.5 * k * dL**2
    e = k1 + k2 + u
    kt1.plot(pos=(t, k1))
    kt2.plot(pos=(t, k2))
    ut.plot(pos=(t, u))
    et.plot(pos=(t, e))

# Plot v-t and a-t graphics
    vt1.plot(pos=(t, b1.v.x))
    vt2.plot(pos=(t, b2.v.x))
    at1.plot(pos=(t, b1.a.x))
    at2.plot(pos=(t, b2.a.x))

# Update time parameter
    t += dt

# Print out the velocity of the blocks after making collision
print(b1.v.x, b2.v.x)