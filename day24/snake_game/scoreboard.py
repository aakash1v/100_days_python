from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')



class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt',mode = 'r') as file:
            self.high_score = int(file.read().strip())
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0,270)
        self.update_score()


    def increase_score(self):
        self.score +=1
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(f"Score = {self.score} || High score= {self.high_score} ", align = ALIGNMENT, font= FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt',mode='w') as file:
                file.write(str(self.high_score))

        self.score = 0
        self.update_score()

    #def gameover(self):
    #    self.goto(0,0)
    #    self.write("GAME OVER  ", align = ALIGNMENT, font= FONT)


        
        
