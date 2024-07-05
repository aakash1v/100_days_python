from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width = 800, height =600)
screen.title('pong')
screen.tracer(0)


r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

#making a middle line..
line = Turtle()
line.penup()
line.hideturtle()
line.goto(0,-300)
line.setheading(90)
for _ in range(30):
    line.pendown()
    line.color('red')
    line.forward(10)
    line.penup()
    line.forward(10)

screen.listen()
screen.onkey(r_paddle.go_up,'Up')
screen.onkey(r_paddle.go_down,'Down')
screen.onkey(l_paddle.go_up,'w')
screen.onkey(l_paddle.go_down,'s')


game_is_on = True
while game_is_on:
    time.sleep(ball.pace)
    screen.update()
    ball.move()

    # detect collission with wall.
    #   bounce ball..
    if ball.ycor() >280 or ball.ycor() <-280:
        ball.bounce_y()

    # detect collision with paddle..
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) <50 and ball.xcor() <-320:
        ball.bounce_x()
        
    # Detect R paddle misses.
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle misses.
    if ball.xcor() < - 380:
        ball.reset_position()
        scoreboard.r_point()

    

screen.exitonclick()
