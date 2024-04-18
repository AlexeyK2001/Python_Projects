from turtle import Turtle, Screen
import random

# ____________________
# random walk of turtle:

# turns = ["left", "right", "none"]
# directions = ["forward", "backward"]
tim = Turtle()
tim.shape("turtle")
tim.color("DarkBlue")
tim.speed(15)
tim.pensize(3)

# def move():
#     if direction == "forward":
#         tim.forward(20)
#     else:
#         tim.backward(20)


# for i in range(1000):
#     r = random.random()
#     g = random.random()
#     b = random.random()
#     tim.pencolor(r, g, b)
#     turn = random.choice(turns)
#     direction = random.choice(directions)
#     if turn == "none":
#         move()
#     elif turn == "left":
#         tim.left(90)
#         move()
#     else:
#         tim.right(90)
#         move()
# ___________________________

# ___________________________
# Draw a spirograph

for i in range(72):
    r = random.random()
    g = random.random()
    b = random.random()
    tim.pencolor(r, g, b)
    tim.circle(120)
    tim.right(5)

screen = Screen()
screen.exitonclick()
