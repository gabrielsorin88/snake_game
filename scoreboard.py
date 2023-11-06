from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 280)
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.score}", move=False, align="center", font=('Arial', 12, 'normal'))

    def update_score(self):
        self.clear()
        self.score += 1
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=('Arial', 12, 'normal'))
