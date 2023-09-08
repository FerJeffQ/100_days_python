from turtle import Turtle, Screen
import random


my_turtle = Turtle()

# Draw a square-----------------------------------------------
# for _ in range(4):
#     my_turtle.forward(100)
#     my_turtle.left(90)


#Draw dashed line---------------------------------------------
# for _ in range(5):
#     my_turtle.forward(15)
#     my_turtle.penup() #no draw when moving
#     my_turtle.forward(10)
#     my_turtle.pendown() #draw when moving
# draw different shapes


# My solution Drawing Different shapes-------------------------------------------------
# side = 3
# cont = 0
# tup = (random.random(), random.random(), random.random())  
# while True:       
#     shape = 360/side #angle of the shape
#     if side < 10: #number of shape            
#         if cont < side:             
#             my_turtle.pencolor(tup)
#             my_turtle.forward(100)
#             my_turtle.right(shape)
#             cont += 1            
#         else:            
#             side += 1
#             cont = 0   
#             tup = (random.random(), random.random(), random.random())       
#     else:        
#         break

# Other Solution Drawing Different shapes ------------------------------------------------------------
# colors = ["aquamarine","spring green","dark turquoise","peru","dark cyan","red","dark magenta", "gold","coral","light sky blue"]
# def draw_shape(num_sides):
#     angle = 360/num_sides
#     for _ in range(num_sides):
#         my_turtle.forward(100)
#         my_turtle.right(angle)

# for shape_side_n in range(3,11):
#     my_turtle.color(random.choice(colors))
#     draw_shape(shape_side_n)

# Draw a Random Walk--------------------------------------------
# angle = [0,90,180,270]
# for _ in range(50):
#     tup = (random.random(), random.random(), random.random()) 
#     my_turtle.pensize(10)
#     my_turtle.speed(9)
#     my_turtle.pencolor(tup)
#     my_turtle.forward(30)    
#     my_turtle.setheading(random.choice(angle))
    
#My solution Draw a spirograph--------------------------------------------
# for _ in range(36):
#     tup = (random.random(), random.random(), random.random()) 
#     my_turtle.pencolor(tup)
#     my_turtle.speed(14)
#     my_turtle.circle(100)
#     my_turtle.right(10)

# Other solution Spirograph
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        my_turtle.speed(14)
        tup = (random.random(), random.random(), random.random()) 
        my_turtle.pencolor(tup)
        my_turtle.circle(100)
        my_turtle.setheading(my_turtle.heading() + size_of_gap)

draw_spirograph(10)        


screen = Screen()
screen.exitonclick()