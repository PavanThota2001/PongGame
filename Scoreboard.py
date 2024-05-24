from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.lscore = 0
        self.rscore = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.show_score()

    def show_score(self):
        self.goto(-100, 230)
        self.write(f"{self.lscore}", align="left", font=('Arial', 40, 'normal'))
        self.goto(100, 230)
        self.write(f"{self.rscore}", align="right", font=('Arial', 40, 'normal'))

    def update_score_left(self):
        self.clear()
        self.lscore += 1
        self.show_score()
    def update_score_right(self):
        self.clear()
        self.rscore += 1
        self.show_score()

    def game_over(self):
        self.color("white")
        self.goto(0, 0)
        self.write("Game Over", align="center", font=('Arial', 20, 'normal'))