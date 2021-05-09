"""
Create a quiz to test if user knows the states of the US
Missing files: image "blank_states_img.gif" and csv file contains state names, x & y coordinates in the image

"""

import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

FONT = ("Verdana", 10, "normal")

game_is_on = True

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []
while game_is_on:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{len(data)} correct states", prompt="What's another state's name?").title()
    state = data[data["state"] == answer_state]
    if state.empty:
        print("not correct")
    else:
        name = state["state"].values[0]
        guessed_states.append(name)

        marker = turtle.Turtle(visible=False)  # our virtual magic marker
        marker.penup()
        marker.color("black")
        marker.goto(x=state["x"].values[0], y=state["y"].values[0])
        marker.write(name, align='center', font=FONT)  # so we can undo it
    if guessed_states == 50:
        game_is_on = False

screen.exitonclick()
