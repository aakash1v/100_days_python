from turtle import Turtle ,Screen
import random

is_race_on =False
screen = Screen()
screen.setup(width=500,height=400)

user_bet = screen.textinput(title='Make your bet.',prompt='Which turtle will win the race? Enter a color: ')
colors = ['red','orange','yellow','green','blue','purple']
y_positions = [-100,-60,-20,20,60,100]
all_turtle=[]

#making finsh_line..
finish_line = Turtle()
finish_line.hideturtle()
finish_line.speed('fastest')
finish_line.penup()
finish_line.goto(x=220,y=-120)
finish_line.setheading(90)

for _ in range(12):
    finish_line.pendown()
    finish_line.forward(10)
    finish_line.penup()
    finish_line.forward(10)

for turtle_index in range(6):
    new_turtle = Turtle(shape = 'turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        step = random.randint(0,10)
        turtle.forward(step)

        if turtle.xcor() >220:
            winner = all_turtle.index(turtle)
            is_race_on = False
            break



    
new = Turtle()
winning_turtle = colors[winner]
new.write(f"{winning_turtle} is winner.", font=("Verdana", 15, "normal"))

if winner == user_bet:
    print(f"You've won! The {winning_turtle} turtle is winner! ")
else:
    print(f"You've lost! The {winning_turtle} turtle is winner!")

screen.exitonclick()
