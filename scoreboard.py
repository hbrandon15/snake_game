from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.color("white")
        self.goto(0, 280)
        self.write(f"Score = {self.score}", align="center", font=('Arial', 15, 'normal'))

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score = {self.score}", align="center", font=('Arial', 15, 'normal'))

