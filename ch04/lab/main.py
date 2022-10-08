import pygame
import random
pygame.init()
pygame.display.set_mode(300,300)

color == (0,0,255)

pygame.draw.rect(255,0,0, pygame.rect(30, 30, 60, 60))
pygame.display.flip()

pygame.draw.circle(0, 255, 0),[300, 300], (170, 3)
pygame.display.flip()
rpoints=[0]
bpoints=[0]
za= [1,2,3,4,5,6]

choicer= input("would you like to be red? Imput your name:")
choiceb= input("would you like to be blue? Imput your name:")
for [i] in za:
  xcoor=randrange(0,300)
  ycoor=randrange(0,300)
  xcoor=int(xcoor)
  ycoor=int(ycoor)
  if [i] in za == 1 or 3 or 5:
    color=255,0,0
  else:
    color=0,0,255

  if xcoor< 150:
   color=0,255,0 
if ycoor< 150:
   color=0,255,0

if color==[0,255,0] and [i] in za == 1 or 3 or 5:
  rpoints = [rpoints +0]

if color==[0,255,0] and [i] in za == 2 or 4 or 6:
  bpoints = bpoints +0

if color==[255,0,0] and [i] in za == 1 or 3 or 5:
  rpoints = rpoints +1

if color==[0,0,255] and [i] in za == 2 or 4 or 6:
  bpoints = bpoints +0
 
pygame.draw.rect(color, pygame.rect(xcoor,ycoor)



if bpoints>rpoints:
 print(choiceb, "WINS")
else:
print(choicer, "WINS")


distance_from_center = math.hypot(x1-x2, y1-y2)
is_in_circle = distance_from_center <= width/2