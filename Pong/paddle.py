#Class to make paddles on both the sides

from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        #Creating paddles for both the sides
        self.shape("square")  #20*20
        self.shapesize(stretch_len= 1, stretch_wid= 5)  #100*20
        self.color("white")
        self.pu()
        self.goto(position)

    #Movement of the paddle
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
