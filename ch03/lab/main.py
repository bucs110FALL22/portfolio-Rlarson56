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
michelangelo.up()
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
## 5. Your PART A code goes here
m_move = random.randrange(1,100)
l_move = random.randrange(1,100)

michelangelo.down()
leonardo.down()

michelangelo.forward(m_move)
leonardo.forward(l_move)

time.sleep(5)

turtle.clear()
michelangelo.up()
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

michelangelo.down()
leonardo.down()
loop=(1,2,3,4,5,6,7,8,9,10)
for(i) in loop:
  m_move = random.randrange(1,10)
  l_move = random.randrange(1,10)
  michelangelo.forward(m_move)
  leonardo.forward(l_move)


# PART B - complete part B here
pygame.init()
window = pygame.display.set_mode()

#triangle
coords=[10,0]
num_sides=(3)
num_sides=int(num_sides)
side_length=(15)
side_length=int(side_length)
offset=(5)
offset=int(offset)

loop2=(1,2,3,4,5,6,7,8,9,10)
for(i) in loop2:
  theta = (2.0 * math.pi * loop2)/num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset


xny=(x,y)
newlist=coords+xny
pygame.display.flip()
pygame.time.wait
window.fill(black)



#square
coords=[20,0]
num_sides=(4)
num_sides=int(num_sides)
side_length=(15)
side_length=int(side_length)
offset=(5)
offset=int(offset)


for(i) in loop2:
  theta = (2.0 * math.pi * loop2)/num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset


xny=(x,y)
newlist=coords+xny
pygame.display.flip()
pygame.time.wait
window.fill(black)


#hexagon
coords=[30,0]
num_sides=(6)
num_sides=int(num_sides)
side_length=(15)
side_length=int(side_length)
offset=(5)
offset=int(offset)


for(i) in loop2:
  theta = (2.0 * math.pi * loop2)/num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset


xny=(x,y)
newlist=coords+xny
pygame.display.flip()
pygame.time.wait
window.fill(black)


#nonagon
coords=[10,-10]
num_sides=(9)
num_sides=int(num_sides)
side_length=(15)
side_length=int(side_length)
offset=(5)
offset=int(offset)


for(i) in loop2:
  theta = (2.0 * math.pi * loop2)/num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset


xny=(x,y)
newlist=coords+xny
pygame.display.flip()
pygame.time.wait
window.fill(black)


#circle
coords=[10,-20]
num_sides=(360)
num_sides=int(num_sides)
side_length=(15)
side_length=int(side_length)
offset=(5)
offset=int(offset)


for(i) in loop2:
  theta = (2.0 * math.pi * loop2)/num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset


xny=(x,y)
newlist=coords+xny
pygame.display.flip()
pygame.time.wait
window.fill(black)



window.exitonclick()
