# import colorgram
from turtle import Screen, Turtle, TurtleScreen, color, forward
import random
turtle = Turtle()
screen = Screen()
screen.colormode(255)
turtle.hideturtle()
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     #rgb_colors.append(color.rgb)
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)
color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

# 10 x 10 rows of spots
# dots should be 20 in size, 50 paces apart
x = -250
y = -250

turtle.penup()
turtle.setx(x)
turtle.sety(y)
turtle.pendown()

for _ in range(10):
    for _ in range(10):
        turtle.dot(20, random.choice(color_list))
        turtle.penup()
        x += 50
        turtle.setx(x)
        turtle.pendown()
        turtle.dot(20, random.choice(color_list))
    turtle.penup()
    y += 50
    turtle.sety(y)
    x = -250
    turtle.setx(x)
    turtle.pendown()

screen.exitonclick()