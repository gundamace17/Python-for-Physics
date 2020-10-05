# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 21:46:44 2020

@author: gunda
"""
"""
In this program, we only demonstrate the terrestrial planets because the volume
of jovian planets are much greater that can make the terrestrials nearly invisible.

"""
from vpython import *

"""
 1. Parameters setup: Below is the data reference from NASA
    Sun     https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html
    Mercury https://nssdc.gsfc.nasa.gov/planetary/factsheet/mercuryfact.html
    Venus   https://nssdc.gsfc.nasa.gov/planetary/factsheet/venusfact.html
    Earth   https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html
    Mars    https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html
"""

# With python dictionary, we can store the parameters of planets and the sun,
# such as radius, mass, d_at_aphelion, v_at_aphelion
radius = {"Mercury": 2439700, "Venus": 6051800, "Earth": 6371000, "Mars": 3389500, "Sun": 696392000}
mass = {"Mercury": 0.33011E24, "Venus": 4.8675E24, "Earth": 5.9723E24, "Mars": 0.64171E24, "Sun": 1988500E24}
#material = {"Mercury": color.cyan, "Venus": color.yellow, "Earth": color.blue, "Mars": color.red, "Sun": color.orange}
d_at_aphelion = {"Mercury": 6982E7, "Venus": 10894E7, "Earth": 15210E7, "Mars": 24923E7}
v_at_aphelion = {"Mercury": 38860, "Venus": 34790, "Earth": 29290, "Mars": 21970}
imgs = {"Mercury": 'Mercury.jpg', 'Venus': 'Venus.jpg', 'Earth': 'Earth.jpg', 'Mars': 'Mars.jpg', 'Sun': 'Sun.jpg'}
G = 6.67408E-11       # Gravitational constant
t = 0                 # Time
dt = 60*60            # Time interval

"""
 2. Use python class to define Planet class:
"""
class Planet:
    def __init__(self, pos, radius, mass, v, img):
        self.pos = pos
        self.radius = radius
        self.mass = mass
        self.texture = img
        self.v = v
        self.a = 0
        self.planet = sphere(pos=self.pos, radius=self.radius, mass=self.mass, 
                             make_trail=True, retain=3650, v=self.v,
                             texture = self.texture)
    def update(self, dt):
        self.dt = dt
        self.a = -G*mass["Sun"] / self.planet.pos.mag2 * self.planet.pos.norm()
        self.v += self.a * self.dt
        self.planet.pos += self.v * self.dt

"""
 3. Window setup:
"""
scene = canvas(title="Planetary Motion", width=600, height=600, x=0, y=0, background=color.black)
sun = sphere(pos=vec(0,0,0), radius=radius["Sun"]*50, color=color.orange, emissive=True, texture = 'Sun.jpg')
lamp = local_light(pos=vec(0,0,0), color=color.white)
# Generate Mercury, Venus, Earth, Mars with for loop
# and capture the data stored in the dictionary above
names = ["Mercury", "Venus", "Earth", "Mars"]
planets = []

for name in names:
    planets.append(Planet(pos=vec(d_at_aphelion[name], 0, 0), radius=radius[name]*2E3, mass=mass[name], 
                          v=vec(0, v_at_aphelion[name], 0), img = imgs[name]))

"""
 4. Set up the motion of planets:
"""
while(True):
    rate(60*24)
    for planet in planets:
        planet.update(dt)
    t += dt