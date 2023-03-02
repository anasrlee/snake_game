from turtle import Turtle

ALIGNEMENT='center'
FONT=('Arial', 24, 'normal')

class Score (Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.color('white')
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f'score: {self.score}', move=False, align=ALIGNEMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write('game over', move=False, align=ALIGNEMENT, font=FONT)

    def increasescore(self):
        self.clear()
        self.score+=1
        self.update_scoreboard()
