from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.penup()
        self.goto(-270,280)
        self.write(f"Level: {self.level}", align="left", font=FONT)
        self.hideturtle()

    def you_lose(self):
        self.penup()
        self.goto(0,0)        
        self.write(f"GAME OVER", align="center", font=FONT)
        self.hideturtle()

        
        
        
        

