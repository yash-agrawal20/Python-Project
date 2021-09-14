#Using Event Listeners
#Date: 14-09-2021

import turtle as t

my_turtle = t.Turtle()

def move_forward():
    my_turtle.forward(50)

def move_backward():
    my_turtle.backward(50)

def move_clockwise():
    my_turtle.right(30)

def move_counter_clockwise():
    my_turtle.left(30)

def clear_screen():
    my_turtle.reset()


screen = t.Screen()
screen.listen()
screen.onkey(fun = move_forward, key = "w")
screen.onkey(fun = move_backward, key = "s")
screen.onkey(fun = move_clockwise, key = "d")
screen.onkey(fun = move_counter_clockwise, key = "a")
screen.onkey(fun = clear_screen, key = "c")
screen.exitonclick()