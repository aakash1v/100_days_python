import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

tim.speed('fastest')

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

def spirograph(angle):

    for i in range(360//angle):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+angle)
        # print(tim.heading())



spirograph(int(input(">")))
screen = t.Screen()
screen.exitonclick()
