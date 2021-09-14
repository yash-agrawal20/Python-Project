#Turtle Race
#Date: 14-09-2021

import turtle as t
import random

is_race_on = False
screen = t.Screen()
screen.setup(width = 500, height = 400)
user_input = screen.textinput(title= "Make a bet", prompt= "Which turtle will win the race?").title()

color = ["red", "orange", "yellow", "blue", "green", "violet"]
y_positions = [-80,-50,-20,10, 40, 70]
all_turtles = []

for turtle_index in range(0,6):
    my_turtle = t.Turtle(shape= "turtle")
    my_turtle.pu()
    my_turtle.color(color[turtle_index])
    my_turtle.goto(x= -230, y= y_positions[turtle_index])
    all_turtles.append(my_turtle)

if user_input:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            first_color = (turtle.pencolor()).title()
            is_race_on = False
        else:
            forward_move = random.randint(5,10)
            turtle.forward(forward_move)


if first_color == user_input:
    print(f"\nYou win! {first_color} turtle has won the race.")
elif first_color != user_input:
    print(f"\nYou lose! {first_color} turtle has won the race.")

screen.exitonclick()