from turtle import Turtle,Screen

tim = Turtle()

def dotted_line():
    for _ in range(15):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()

dotted_line()

screen = Screen()
screen.exitonclick()
