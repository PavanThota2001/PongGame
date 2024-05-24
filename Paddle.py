from turtle import Turtle
class paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.UP()
        self.DOWN()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, y)
    def UP(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    def DOWN(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


