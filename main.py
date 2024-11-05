# Introduction to VPython

# importing vpython module
from vpython import *
from time import *
import numpy as np

scene = canvas(width=1000, height=800, background=color.gray(0.3))

piston = cylinder(radius=1, length=3, color=color.red, opacity=0.5)

while True:
    for o in np.linspace(0,1,100):
        rate(50)
        piston.opacity = o
    for o in np.linspace(1,0,100):
        rate(50)
        piston.opacity = o