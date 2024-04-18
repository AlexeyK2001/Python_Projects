from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_backward():
    tim.pendown()
    tim.backward(10)


def move_forward():
    tim.pendown()
    tim.forward(10)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


def overall_move():
    global choice


def clear():
    tim.clear()
    tim.penup()
    tim.home()


screen.listen()
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
