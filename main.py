# Introduction to VPython

# importing vpython module
from vpython import *
from time import *

scene = canvas(width=1000, height=800, background=color.gray(0.3))

floor       = box(pos=vector(0,-10,0), color=color.white, size=vector(20,.3,20))
ceiling     = box(pos=vector(0,10,0),  color=color.white, size=vector(20,.3,20))
right_wall  = box(pos=vector(10,0,0),  color=color.white, size=vector(.2,20,20))
left_wall   = box(pos=vector(-10,0,0), color=color.white, size=vector(.2,20,20))
back_wall   = box(pos=vector(0,0,-10), color=color.white, size=vector(20,20,.3))

marble      = sphere(color=color.red, radius=3)

changeX = 0.1
xPos = 0

while True:
    rate(20) # To change the speed of animation

    xPos = xPos + changeX

    if xPos > 10 or xPos < -10:
        changeX *= -1

    marble.pos = vector(xPos,0,0)