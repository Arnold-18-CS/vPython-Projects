# Introduction to VPython

# importing vpython module
from vpython import *
from time import *
import random

scene = canvas(width=1000, height=800, background=color.gray(0.3))
xPos, yPos, zPos = 0, 0, 0

mRadius = 1
wallThickness = .3
roomWidth, roomHeight, roomDepth = 20,20,30

floor       = box(pos=vector(0,-roomHeight/2,0), color=color.white, size=vector(roomWidth,wallThickness,roomDepth))
ceiling     = box(pos=vector(0,roomHeight/2,0),  color=color.white, size=vector(roomWidth,wallThickness,roomDepth))
right_wall  = box(pos=vector(roomWidth/2,0,0),  color=color.white, size=vector(wallThickness,roomHeight,roomDepth))
left_wall   = box(pos=vector(-roomWidth/2,0,0), color=color.white, size=vector(wallThickness,roomHeight,roomDepth))
back_wall   = box(pos=vector(0,0,-roomDepth/2), color=color.white, size=vector(roomWidth,roomHeight,wallThickness))
# front_wall   = box(pos=vector(0,0,roomDepth/2), color=color.white, size=vector(roomWidth,roomHeight,wallThickness))

marble      = sphere(pos=vector(xPos, yPos, zPos),color=color.red, radius=mRadius)

changeX, changeY, changeZ = .1, .1, .1

while True:
    rate(30) # To change the speed of animation
   
    xPos += changeX
    yPos += changeY
    zPos += changeZ

    xRMEdge = xPos + mRadius
    xLMEdge = xPos - mRadius
    yTMEdge = yPos + mRadius
    yBMEdge = yPos - mRadius
    zBMEdge = zPos + mRadius
    zFMEdge = zPos - mRadius

    RWEdge = roomWidth / 2 - wallThickness / 2
    LWEdge = -roomWidth / 2 + wallThickness / 2
    CEdge = roomHeight / 2 - wallThickness / 2
    FlEdge = -roomHeight / 2 + wallThickness / 2
    BEdge = roomDepth / 2 + wallThickness / 2
    FrEdge = - roomDepth / 2 + wallThickness / 2

    if xRMEdge > RWEdge or xLMEdge < LWEdge:
            changeX *= -1

    if yTMEdge > CEdge or yBMEdge < FlEdge:
            changeY *= -1

    if zBMEdge > BEdge or zFMEdge < FrEdge:
            changeZ *= -1 

    marble.pos = vector(xPos,yPos,zPos)