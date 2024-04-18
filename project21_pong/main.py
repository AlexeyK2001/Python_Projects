# COMPONENTS:
# Score, player bars and their movement, ball
from turtle import Screen, Turtle
from paddles import Paddle
from ball import Ball
from Score import Score
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

screen.tracer(0)


rpaddle = Paddle((350, 0))
lpaddle = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkeypress(rpaddle.go_up, "Up")
screen.onkeypress(rpaddle.go_down, "Down")
screen.onkeypress(lpaddle.go_up, "w")
screen.onkeypress(lpaddle.go_down, "s")

game_is_on = True
while game_is_on:
    score.update_scoreboard()
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collission with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with the paddle
    if (
        ball.distance(rpaddle) < 50
        and ball.xcor() > 325
        or ball.distance(lpaddle) < 50
        and ball.xcor() < -325
    ):
        ball.bounce_x()
    # Detect if the ball goes out of bounds
    if ball.xcor() > 370:
        score.increase_first()
        ball.reset_position()
    elif ball.xcor() < -370:
        score.increase_second()
        ball.reset_position()
    # Detect if the game is over
    if score.score_first_player == 7 or score.score_second_player == 7:
        score.game_over()
        game_is_on = False

screen.exitonclick()
