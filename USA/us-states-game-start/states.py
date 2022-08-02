from turtle import Turtle



class States(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()

    def state_create(self, name, x, y):
        self.goto(x, y)
        self.write(f"{name}")

    def check(self, answer, name_states):
        if answer in name_states:
            return True
        else:
            return False







