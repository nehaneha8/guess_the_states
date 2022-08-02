from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Times New Roman', 12, 'bold')
TU_FONT = ('Times New Roman', 40, 'bold')
GO_FONT = ('Times New Roman', 40, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        with open("state_high.txt") as file:
            self.highscore = int(file.read())

        self.goto(0, 250)
        self.score = 0
        self.update()

    def update(self):
        self.clear()
        self.write(f"{self.score} / 50 States found "
                   f"       High Score {self.highscore} ",
                   align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("state_high.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.update()

    def increase(self):
        self.score += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=GO_FONT)






