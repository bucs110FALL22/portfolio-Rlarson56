import turtle

my_turtle=turtle.Turtle()

my_turtle.shape("turtle")
my_turtle.color("black")


num_sides=input("How many sides would you like your shape to have..  ")
num_sides=int(num_sides)
length=input("How long would you like each sides of your shape to be..  ")
length=int(length)
angle=360/num_sides
angle=int(angle)
for i in [angle]*num_sides:
  my_turtle.forward(length)
  my_turtle.right(i)


turtle.Screen().exitonclick()