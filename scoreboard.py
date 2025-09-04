from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.high_score = self.read_high_score()
        self.color("white")
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.update_high_score()
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def read_high_score(self):
        with open("data.txt") as data:
            return int(data.read())

    def update_high_score(self):
        with open("data.txt", mode="w") as data:
            data.write(f"{self.score}")



