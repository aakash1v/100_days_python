import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

directions = [0,90,180,270]
tim.speed('fastest')
tim.pensize(10)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

def generate_line()
    for i in range(200):
        tim.color(random_color())
        tim.setheading(random.choice(directions))
        tim.forward(30)


t.screen = Screen()
t.screen.exitonclick()
