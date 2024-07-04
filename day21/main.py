from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Score

import time

screen = Screen()
screen.setup(height=600,width=600)
screen.bgcolor('black')
screen.title('MY Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.right,'Right')
screen.onkey(snake.left,'Left')


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    
    snake.move()
    
    # detect collission the food..
    if snake.head.distance(food) <15:
        food.refresh()
        score.increase_score()
        snake.extend()

    # detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() <-290 or snake.head.ycor() >290 or snake.head.ycor() <-290:
        game_is_on = False
        score.gameover()

    # detect collision with tail..
    # if head collides with any segment in the tail:
    #       trigger game_over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) <10:
            score.gameove()
            game_is_on = False


screen.exitonclick()
