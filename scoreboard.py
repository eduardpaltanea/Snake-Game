from turtle import Turtle
FONT = ('Arial', 20, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=0,y=270)
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=FONT)
    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"Game over", move=False, align="center", font=FONT)