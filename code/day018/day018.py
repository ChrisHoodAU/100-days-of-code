from turtle import Screen, Turtle, TurtleScreen, color, forward
import random

turtle = Turtle()

turtle.shape("turtle")
turtle.color("green")

def change_color():
    R = random.random()
    G = random.random()
    B = random.random()
    # turtle.color(R, G, B)
    return (R, G, B)

def draw_shape(num_sides):
    angle = 360 / num_sides
    change_color()
    for _ in range(num_sides):
        turtle.forward(100)
        turtle.right(angle)

def random_direction():
    directions = [0, 90, 180, 270]
    return random.choice(directions)

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        turtle.color(change_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + size_of_gap)

#square
# for _ in range(4):
#     turtle.forward(100)
#     turtle.right(90)

#dashed line
# for _ in range(15):
#     turtle.pendown()
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)

#different shapes - each angle is 360 / sides
#triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon
# for sides in range(3,11):
#     angle = 360 / sides
#     change_color()
#     for _ in range(sides):
#         turtle.color()
#         turtle.forward(100)
#         turtle.right(angle)

# for sides in range(3,11):
#     draw_shape(sides)

# Draw a random walk
# turtle.pensize(10)
# turtle.speed(0)
# for _ in range(100):
#     # change_color()
#     turtle.color(change_color())
#     turtle.setheading(random_direction())
#     # turtle.setheading(random.choice(directions)) #simpler than the function 
#     turtle.forward(30)

# Spirograph
# 100 diameter circle
# change tilt
turtle.speed(0)
draw_spirograph(5)

screen = Screen()
screen.exitonclick()