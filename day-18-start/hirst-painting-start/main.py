###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
# import colorgram
# rgb_colors = []
# colors = colorgram.extract('./image.jpg', 30)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

from turtle import Turtle, Screen
import random
import turtle

turtle.colormode(255)
color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
my_turtle = Turtle()

def move_turtle(diameter,step,num_points):  
    jump =  step
    for _ in range(num_points):
        my_turtle.penup()
        my_turtle.goto((0, jump - 200))
        jump += 50
        for _ in range(num_points):    
            my_turtle.pencolor(random.choice(color_list))          
            my_turtle.dot(diameter)
            my_turtle.penup()
            my_turtle.forward(step) 
        
move_turtle(20,50,10)  




screen = Screen()
screen.exitonclick()