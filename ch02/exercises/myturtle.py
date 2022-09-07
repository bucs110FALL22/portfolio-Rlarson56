import turtle

my_turtle=turtle.Turtle()

my_turtle.shape("turtle")
my_turtle.color("purple")


num_sides=4
legnth=50
angle=360/num_sides
for i in [angle]*num_sides:
  my_turtle.forward(legnth)
  my_turtle.right(i)

legnth=20
my_turtle.color("white")
angle=360/num_sides
my_turtle.left(i)
my_turtle.forward(legnth)
my_turtle.color("red")
for i in [angle]*num_sides:
  my_turtle.forward(legnth)
  my_turtle.left(i)
turtle.Screen().exitonclick()