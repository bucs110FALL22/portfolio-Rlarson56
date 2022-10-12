## cd ch04/exercises
## python3 coinflip.py
import turtle
import random

a_turtle=turtle.Turtle()
a_turtle.shape("turtle")
a_turtle.color("black")
a_turtle.setpos(0,0)
window=turtle.Screen()
turtle.screensize(canvwidth=200, canvheight=200, bg="white")
canvwidth=turtle.window_width()
canvheight=turtle.window_height()

while a_turtle.xcor() < 100 and  a_turtle.ycor()< 100:
 side=random.randrange(0,2)
 side=int(side)
 if side == 1:
     a_turtle.left(90)
     print("HEADS")
 else:
     a_turtle.right(90)
     print("TAILS")
 a_turtle.forward(20)


turtle.Screen().bgcolor("yellow")
turtle.Screen().exitonclick()

