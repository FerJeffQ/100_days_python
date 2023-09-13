from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):                
        self.pos_x = 350
        self.pos_y = 0
        self.create_player()

    def create_player(self):               
        segment = Turtle()
        segment.shape("square")
        segment.shapesize(stretch_wid=5,stretch_len=1)
        segment.penup()
        segment.color("white")
        segment.goto(350,0)



        
            
          
            
        
