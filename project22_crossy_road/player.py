from turtle import Turtle
import time

STARTING_POSITION = (0, -270)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.left(90)
        self.shape("turtle")
        self.goto(STARTING_POSITION)

    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def finish(self):
        self.goto(STARTING_POSITION)

    def stop_by_hitting(self):
        self.goto(self.xcor(), self.ycor())
