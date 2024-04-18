import colorgram
import turtle as t
from turtle import Turtle, Screen
import random as r

t.colormode(255)
# colors = colorgram.extract("image.jpg", 25)
color_list = [
    (229, 228, 226),
    (225, 223, 224),
    (199, 175, 117),
    (124, 36, 24),
    (210, 221, 213),
    (168, 106, 57),
    (222, 224, 227),
    (186, 158, 53),
    (6, 57, 83),
    (109, 67, 85),
    (113, 161, 175),
    (22, 122, 174),
    (64, 153, 138),
    (39, 36, 36),
    (76, 40, 48),
    (9, 67, 47),
    (90, 141, 53),
    (181, 96, 79),
    (132, 40, 42),
    (210, 200, 151),
    (141, 171, 155),
    (179, 201, 186),
    (172, 153, 159),
    (212, 183, 177),
    (176, 198, 203),
]
# for i in range(len(colors)):
#     the_color = colors[i]
#     tuple1 = (the_color.rgb.r, the_color.rgb.g, the_color.rgb.b)
#     color_list.append(tuple1)
# print(color_list)
tim = Turtle()
tim.penup()
tim.hideturtle()
tim.setpos(-200, -200)
tim.speed(15)
tim.shape("turtle")
for i in range(10):
    for j in range(10):
        tim.dot(20, r.choice(color_list))
        if j < 9:
            tim.forward(50)
    tim.left(180)
    tim.forward(450)
    tim.right(90)
    tim.forward(50)
    tim.right(90)

screen = Screen()
screen.exitonclick()
