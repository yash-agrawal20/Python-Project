#Date: 09-09-2021
#Extracting color from a image

# import colorgram
# colors = colorgram.extract('image_hirst.jpg',30)
# # print(colors)
# rgb_color = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_color.append(new_color)

# # print(rgb_color)

import turtle as t
import random

turtle_main = t.Turtle()
t.colormode(255)
#Extracting color list using the above program
color_list = [(253, 252, 241), (238, 250, 244), (187, 18, 44), (243, 231, 66), (252, 235, 239), (210, 236, 242), (196, 75, 32), (218, 66, 107), (17, 124, 173), (196, 175, 17), (108, 181, 209), (12, 142, 88), (12, 166, 214), (210, 152, 96), (187, 41, 61), (241, 231, 2), (23, 39, 76), (77, 174, 94), (36, 44, 112), (215, 69, 50), (218, 130, 155), (124, 185, 119), (235, 165, 183), (5, 58, 39), (146, 209, 220), (8, 95, 55), (4, 86, 111), (162, 29, 27), (234, 171, 164), (162, 212, 176)]
#pu -> penup
turtle_main.pu()
turtle_main.hideturtle()
#seth -> setheading
turtle_main.seth(225)
turtle_main.forward(300)
turtle_main.seth(0)
number_of_dots = 100

for count_dots in range(1, number_of_dots+1):
    turtle_main.dot(20,random.choice(color_list))
    turtle_main.forward(50)
    
    if count_dots % 10 == 0:
        turtle_main.seth(90)
        turtle_main.forward(50)
        turtle_main.seth(180)
        turtle_main.forward(500)
        turtle_main.seth(0)





screen = t.Screen()
screen.exitonclick()