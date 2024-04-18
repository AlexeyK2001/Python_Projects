from turtle import Turtle

ALIGMNENT = "center"
FONT = ("Courier", 24, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.score_first_player = 0
        self.score_second_player = 0
        self.goto(0, 260)
        self.hideturtle()

    def update_scoreboard(self):
        self.write(
            f"{self.score_first_player} : {self.score_second_player}",
            move=False,
            align=ALIGMNENT,
            font=FONT,
        )

    def increase_first(self):
        self.score_first_player += 1
        self.clear()
        self.update_scoreboard()

    def increase_second(self):
        self.score_second_player += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        if self.score_first_player == 7:
            self.write(
                f"First player wins",
                move=False,
                align=ALIGMNENT,
                font=FONT,
            )

        if self.score_second_player == 7:
            self.write(
                f"Second player wins",
                move=False,
                align=ALIGMNENT,
                font=FONT,
            )
