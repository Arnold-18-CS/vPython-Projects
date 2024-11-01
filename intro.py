# Introduction to VPython

# importing vpython module
from vpython import *
from time import *

ball = sphere()
sleep(5)
ball.color = color.red
sleep(5)
ball.color = color.blue
while True:
    pass