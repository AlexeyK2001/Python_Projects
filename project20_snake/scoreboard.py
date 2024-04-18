from turtle import Turtle

ALIGMNENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.score_number = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score_number} Highest score: {self.high_score}",
            move=False,
            align=ALIGMNENT,
            font=FONT,
        )

    def increase_score(self):
        self.score_number += 1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        if self.score_number > self.high_score:
            self.high_score = self.score_number
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score_number = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(
    #         f"GAME OVER",
    #         move=False,
    #         align=ALIGMNENT,
    #         font=FONT,
    #     )
