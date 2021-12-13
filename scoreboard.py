from turtle import Turtle
FONT = ("Courier", 24, "normal")
FONT2 = ("Courier", 15, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.level = 1
        self.update()

    def update(self):
        self.reset()
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.write(f"Score:{self.score} Level:{self.level}",align="center", font=FONT)

    def next_level(self):
        self.score += 1
        self.level += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("Your turtle got squashed! Game Over", align="center", font=FONT2)

