#PONG
#Date: 16-09-2021

import turtle as t
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = t.Screen()
screen.setup(width= 800, height= 600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)
 
#Creating the paddle on the right side
right_paddle = Paddle((380, 0))
left_paddle = Paddle((-380, 0))
ball = Ball()
scoreboard = Scoreboard()

#Movement of the paddle
screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()
    
    #When the ball hits the upper and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 360:
        ball.bounce_x()

    #Detect collision with left paddle
    elif ball.distance(left_paddle) < 50 and ball.xcor() < -360:
        ball.bounce_x()

    #Reset Position
    elif ball.xcor() > 410:
        time.sleep(1)
        ball.goto(x = 0, y = 0)
        ball.bounce_x()
        scoreboard.l_point()

    elif ball.xcor() < -410:
        time.sleep(1)
        ball.goto(x = 0, y = 0)
        ball.bounce_x()
        scoreboard.r_point()


screen.exitonclick()