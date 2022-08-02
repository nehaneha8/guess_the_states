from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Times New Roman', 12, 'bold')


class Strike(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.color("red")
        self.goto(0, 280)
        self.strike_num = 0
        self.strike_update()

    def strike_update(self):
        self.clear()
        self.write(f"{self.strike_num} / 3 Strikes",
                   align=ALIGNMENT, font=FONT)

    def strikes(self):
        strike = Turtle()
        strike.penup()
        strike.ht()
        strike.color("red")
        strike.goto(0, -10)
        self.write(f"{self.strike_num} / 3 Strikes",
                   align=ALIGNMENT, font=FONT)

    def increase(self):
        self.strike_num += 1
        self.strike_update()
        if self.strike_num == 3:
            return True
        else:
            return False


