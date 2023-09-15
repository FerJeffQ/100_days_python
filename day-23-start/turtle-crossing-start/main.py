import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
cont = 0
cars = []
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_cars()
    car_manager.move_cars()

    #detect you win
    if player.you_win():        
        scoreboard.level += 1
        car_manager.car_speed += 10
    else:        
        scoreboard.update_score()

    
    #detect collision car
    for car in car_manager.all_cars:
        distance = player.distance(car)
        if distance < 20:            
            game_is_on = False
            scoreboard.you_lose()
            print("lose")

    
      

screen.exitonclick()            


