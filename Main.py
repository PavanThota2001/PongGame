from turtle import Turtle, Screen
from Paddle import paddle
from Ball import ball
import time
from Scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.setup(width = 800, height= 600)
screen.bgcolor("black")
screen.title("pong game")
r_paddle = paddle(350, 0)
l_paddle = paddle(-350, 0)
screen.listen()
screen.onkey(r_paddle.UP, "Up")
screen.onkey(r_paddle.DOWN, "Down")
screen.onkey(l_paddle.UP, "w")
screen.onkey(l_paddle.DOWN, "s")
ball = ball()
scoreboard = Scoreboard()
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.update_score_left()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.update_score_right()
    if scoreboard.rscore == 3 or scoreboard.lscore == 3:
        scoreboard.game_over()
        game_on = False
screen.exitonclick()
