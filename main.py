# Introduction to VPython

# importing vpython module
from vpython import *
from time import *
import numpy as np

scene = canvas(width=1000, height=800, background=color.gray(0.3))

# Creating a thermometer
bulb = sphere(radius=1.25, color=color.white, opacity=.4)
tube = cylinder(radius=0.6, length=5, color=color.white, opacity=.4)
mercuryInBulb = sphere(radius=1, color=color.red, opacity=1)
mercuryCol = cylinder(radius=0.5, length=4.5, color=color.red, opacity=1)

while True:
        for temp in np.linspace(1,5,100):
                rate(20)
                mercuryCol.length = temp
        for temp in np.linspace(5,1,100):
                rate(20)
                mercuryCol.length = temp