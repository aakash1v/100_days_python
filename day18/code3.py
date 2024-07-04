from turtle import Turtle,Screen
import random 


tim =Turtle()
colors = ['medium sea green','deep sky blue','orange','orchid','orange red','yellow','medium purple']
n = len(colors)

def draw_shape(num_sides):
    angle = 360/num_sides
    
    for _ in range(num_sides):
        tim.color(color_name)
        tim.forward(100)
        tim.right(angle)

for i in range(3,11):
    color_name = colors[random.randint(1,n-1)]
    draw_shape(i)

screen = Screen()
screen.exitonclick()
