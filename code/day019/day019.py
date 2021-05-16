from turtle import Turtle, Screen
turtle = Turtle()
screen = Screen()


def move_forwards():
    turtle.forward(10)

def move_backwards():
    turtle.backward(10)

def turn_left():
    turtle.left(10)

def turn_right():
    turtle.right(10)

def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()

screen.listen()
#screen.onkey(key="space", fun=move_forwards) #don't add the parenthesis when you're passing a function as a parameter
# w a s d, c to clear
screen.onkey(key="c", fun=clear)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.exitonclick()