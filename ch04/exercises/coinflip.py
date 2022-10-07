import turtle
import random

a_turtle=turtle.Turtle()
a_turtle.shape("turtle")
a_turtle.color("black")
a_turtle.home()

xc=a_turtle.xcor()
yc=a_turtle.ycor()

while 100>xc>-100 and 100>yc>-100:
 side==randrange(0,1) 
  if side == 0: 
    a_turtle.left(90)
   elif side == 1:
    a_turtle.right(90)
  a_turtle.foward(20)




turtle.Screen().exitonclick()

