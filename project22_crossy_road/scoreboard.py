from turtle import Turtle
import time

ALIGMNENT = "left"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.current_level = 0
        self.goto(-270, 265)
        self.hideturtle()

    def update_description(self):
        self.write(
            f"Level: {self.current_level}",
            move=False,
            align=ALIGMNENT,
            font=FONT,
        )

    def update_level(self):
        self.current_level += 1
        self.clear()
        self.update_description()

    def game_over(self):
        self.goto(0, 0)
        self.write(
            f"Game Over.",
            move=False,
            align="center",
            font=FONT,
        )
