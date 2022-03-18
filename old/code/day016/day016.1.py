# import turtle
# timmy = turtle.Turtle()

from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)

my_screen = Screen()
#attributes
print(my_screen.canvheight)
print(my_screen.canvwidth)
#methods
timmy.shape('turtle')
timmy.color('chartreuse2')
timmy.forward(100)
my_screen.exitonclick()
