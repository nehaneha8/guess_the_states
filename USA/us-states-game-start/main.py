import turtle
import pandas
from states import States
from scoreboard import Scoreboard
from strikes import Strike
import time

screen = turtle.Screen()
screen.title("USA States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

full_list = pandas.read_csv("50_states.csv")

state_list = (full_list["state"]).to_list()

states = States()

scoreboard = Scoreboard()

strike = Strike()

game_is_on = True
empty = []
while game_is_on:
    answer = (screen.textinput("Guess The State", "Enter a state...")).title()

    if states.check(answer, state_list):
        all_info = full_list[full_list["state"] == answer]
        x = float(all_info.x)
        y = float(all_info.y)
        states.state_create(answer, x, y)
        scoreboard.increase()


    else:
        if strike.increase():
            scoreboard.reset()
            scoreboard.game_over()
            game_is_on = False
        else:
            pass

    screen.update()

screen.exitonclick()


# empty map
# ask for state
# if state is correct, it appears
#
#
#
#
#
#
#
#
#
#
#
#
#
#
