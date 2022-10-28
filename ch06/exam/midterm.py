###python3 midterm.py
##cd ch06/exam
##turtle.Screen().exitonclick()
import turtle
back = turtle.Screen()
back.setup(width=500, height=400)
back.bgcolor('grey')
turt=turtle.Turtle()
turt.width(10)
turt.speed(10)
turt.hideturtle()
ORANGE = 'orange'
WHITE = 'white'
YELLOW = 'yellow'
GREY = 'grey'
stick_start= (0,-70)
spiral_start=(0,80)

def main(): #main
  def draw_circle(linecolor): #function to draw the circle in the picture
    turt.color(linecolor)
    turt.begin_fill()
    turt.circle(80)
    turt.end_fill()

  def stick(line): #fuction for the stick
    turt.penup()
    turt.goto(stick_start)
    turt.pendown()
    turt.color(line)
    turt.left(90)
    turt.forward(100)

  def spiral(inside): #function for the spiral
    turt.penup()
    turt.goto(spiral_start)
    turt.pendown()
    turt.color(inside)
    for i in range(40): #loops to create spiral
      turt.forward(i)
      turt.right(30)

  #calls all 3 functions
  draw_circle(ORANGE)
  stick(WHITE)
  spiral(YELLOW)

main() #execute main

def clicking_action(mousex,mousey): #fuction that activates when mouse is clicked
  turt.penup()
  turt.left(33)
  turt.color(GREY)
  turt.goto(mousex,mousey) #turtle goes to coords of mouse click
  turt.pendown()
  turt.begin_fill()
  turt.circle(16)
  turt.end_fill()
  return clicking_action #returns the coords of the click

back.onclick(clicking_action) #detects clicks and carries out clicking_action function
back.mainloop() #keeps window open 
