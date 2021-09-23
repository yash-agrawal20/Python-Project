#Creatin the ball and then moving it

from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        self.x_move = 10
        self.y_move = 10

    def bounce_y(self):
        self.y_move *= -1 

    def bounce_x(self):
        self.x_move *= -1       

    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)



