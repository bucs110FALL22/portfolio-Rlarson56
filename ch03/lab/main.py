##cd ch03/lab
## python3 main.py
import turtle #1. import modules
import random
import time
import pygame
import math

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

# 4. Pick up the pen so we don’t get lines
def reset():
  turtle.clear()
  michelangelo.up()
  leonardo.up()
  michelangelo.goto(0,10)
  leonardo.goto(0,0)
## 5. Your PART A code goes here
m_move = random.randrange(1,100)
l_move = random.randrange(1,100)
reset()
michelangelo.down()
leonardo.down()

michelangelo.forward(m_move)
leonardo.forward(l_move)

time.sleep(5)

reset()

michelangelo.down()
leonardo.down()
loop=(1,2,3,4,5,6,7,8,9,10)

for i in loop:
  m_move = random.randrange(1,10)
  l_move = random.randrange(1,10)
  michelangelo.forward(m_move)
  leonardo.forward(l_move)


# PART B - complete part B here
pygame.init()


#triangle
coords=[]
num_sides= 3
side_length= 15
offset= 5

loop2=(1,2,3)



for i in loop2:
  theta = (2.0 * math.pi * i in loop)/num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append((x,y))
pygame.display.polygon(window,red,coords)
pygame.display.flip()


reset()
pygame.time.wait(40)

#square
coords=[]
num_sides= 4
side_length= 15
offset= 6

loop2=(1,2,3,4)



for i in loop2:
  theta = (2.0 * math.pi * i)/num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append((x,y))

pygame.display.flip()


reset()
pygame.time.wait(40)

#hexagon
coords=[]
num_sides= 6
side_length= 15
offset= 7

loop2=(1,2,3,4,5,6)


for i in loop2:
  theta = (2.0 * math.pi * i)/num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append((x,y))

pygame.display.flip()


reset()
pygame.time.wait(40)

#nonagon
coords=[]
num_sides= 9
side_length= 15
offset= 8

loop2=(1,2,3,4,5,6,7,8,9)



for i in loop2:
  theta = (2.0 * math.pi * i)/num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append((x,y))
pygame.display.polygon(window,red,coords)
pygame.display.flip()


reset()
pygame.time.wait(40)

#circle
coords=[]
num_sides= 360
side_length= 15
offset= 8

loop2=range(1,360)



for i in loop2:
  theta = (2.0 * math.pi * i)/num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append((x,y))
pygame.display.polygon(window,red,coords)
pygame.display.flip()


reset()
pygame.time.wait(40)


##need help displaying polygons