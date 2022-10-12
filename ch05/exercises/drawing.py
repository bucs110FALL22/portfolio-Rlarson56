## cd ch05/exercises
## python3 drawing.py
import turtle
num_sides=0
side_length=0

def drawEqShape(turt,num_sides,side_length):
 num_sides=input("How many sides would you like your shape to have ")
 num_sides=int(num_sides)
 side_length=input("How long would you like each side to  be..  ")
 side_length=int(side_length)
 angle=360/num_sides
 angle=int(angle)
 for i in [angle]*num_sides:
  turt.forward(side_length)
  turt.right(i)
   

turt=turtle.Turtle()
turt.shape("turtle")
turt.color("green")
turt.setpos(0,0)
window=turtle.Screen()
turtle.screensize(canvwidth=200, canvheight=200, bg="white")
canvwidth=turtle.window_width()
canvheight=turtle.window_height()

drawEqShape(turt,num_sides,side_length)
turtle.Screen().exitonclick()