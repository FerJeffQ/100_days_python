from turtle import Turtle
import random
LIMIT = 270
class Food(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle") # you can change this shape 
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("yellow")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        self.goto(random.randint(-LIMIT,LIMIT),random.randint(-LIMIT,LIMIT))

    

    