from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 10, 'bold')

with open('high_score.txt', 'r') as file:
    HIGH_SCORE = int(file.read())


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.score = 0
        self.high_score = HIGH_SCORE

    def reset_sb(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('high_score.txt', 'w') as data:
                data.write(str(self.score))
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, ALIGNMENT, FONT)
