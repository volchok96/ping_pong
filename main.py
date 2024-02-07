from turtle import Screen
from pad import Pad
from scoreboard import Scoreboard
from ball import Ball
from time import sleep

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping-Pong")
screen.tracer(0)

l_pad = Pad((-350, 0))
r_pad = Pad((350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_pad.up, "Up")
screen.onkey(r_pad.down, "Down")
screen.onkey(l_pad.up, "w")
screen.onkey(l_pad.down, "s")

game_is_on = True
while game_is_on:
    sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_pad) < 50 and ball.xcor() > 320 or ball.distance(l_pad) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()