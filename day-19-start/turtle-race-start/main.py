from turtle import Turtle, Screen
import random

screen = Screen()

is_race_on = False
screen.setup(height=400, width=500)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red","orange","yellow","green","blue","purple"]

turtles = []
y_ini = -120
for num in range(6):
    turtles.append(Turtle(shape="turtle"))
    turtles[num].penup()
    turtles[num].color(colors[num])
    turtles[num].goto(x=-230,y=y_ini)
    y_ini +=50
 
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:        
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)        
        if turtle.xcor() > 230: 
            _,color_turtle = turtle.color()           
            if user_bet == color_turtle:
                print(f"You've won, the turtle wins is {color_turtle}")
            else:
                print(f"You've lose because the turtle wins is {color_turtle}")
            is_race_on = False
    


screen.exitonclick()