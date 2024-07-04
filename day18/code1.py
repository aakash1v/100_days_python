from turtle import Turtle,Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.color('blue')
timmy_the_turtle.shape('turtle')

def one_step():
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)

def square():
    for i in range(4):
        one_step()

square()


screen = Screen()
screen.exitonclick()

