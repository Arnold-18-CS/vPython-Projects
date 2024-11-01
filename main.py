# Introduction to VPython

# importing vpython module
from vpython import *
from time import *

scene = canvas(width=1000, height=800, background=color.gray(0.3))

mRadius = 1
wallThickness = .3
roomWidth, roomDepth, roomHeight = 20,20,20

floor       = box(pos=vector(0,-roomHeight/2,0), color=color.white, size=vector(roomWidth,wallThickness,roomDepth))
ceiling     = box(pos=vector(0,roomHeight/2,0),  color=color.white, size=vector(roomWidth,wallThickness,roomDepth))
right_wall  = box(pos=vector(roomWidth/2,0,0),  color=color.white, size=vector(wallThickness,roomHeight,roomDepth))
left_wall   = box(pos=vector(-roomWidth/2,0,0), color=color.white, size=vector(wallThickness,roomHeight,roomDepth))
back_wall   = box(pos=vector(0,0,-roomDepth/2), color=color.white, size=vector(roomWidth,roomHeight,wallThickness))

marble      = sphere(color=color.red, radius=mRadius)

changeX = 0.1
xPos = 0

while True:
    rate(30) # To change the speed of animation

    xPos = xPos + changeX

    if xPos+mRadius+wallThickness > 10 or xPos-mRadius-wallThickness < -10:
        changeX *= -1

    marble.pos = vector(xPos,0,0)