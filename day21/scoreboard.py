from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.SCORE = 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0,270)
        self.update_score()


    def increase_score(self):
        self.SCORE +=1
        self.clear()
        self.update_score()
        
    def update_score(self):
        self.write(f"score = {self.SCORE} ", align = ALIGNMENT, font= FONT)

    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER  ", align = ALIGNMENT, font= FONT)


        
        
