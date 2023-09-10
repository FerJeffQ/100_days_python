from turtle import Turtle
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.pos_x = 0
        self.pos_y = 0
        self.flag_create = True
        self.generate_snake()
        self.head = self.segments[0]

    def generate_snake(self):
        for _ in range(3):    
            self.add_segment()    
        self.flag_create = False


    def add_segment(self):

        if self.flag_create == True:
            self.pos_x += -MOVE_DISTANCE
        else:                      
            self.pos_x = self.segments[-1].xcor()
            self.pos_y = self.segments[-1].ycor()        
            
        segment = Turtle("square")        
        segment.color("white")
        segment.shapesize(stretch_len=0.8,stretch_wid=0.8)
        segment.penup()
        segment.goto(self.pos_x,self.pos_y)    
        self.segments.append(segment)



            



    def up(self):
        if self.head.heading() != 270.0:
            self.head.setheading(90)                    
        
    def down(self):
        if self.head.heading() != 90.0:
            self.head.setheading(270)            
        
    def left(self):
        if self.head.heading() != 0.0:
            self.head.setheading(180)            
        
    def right(self):
        if self.head.heading() != 180.0:
            self.head.setheading(0)            

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            #new coordinates
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x,new_y)  

        self.head.forward(MOVE_DISTANCE)