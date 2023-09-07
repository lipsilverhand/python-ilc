import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#Create screen for the game
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#Create player, car manager and scoreboard
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

#Set key arrow up, right, down for player
screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_right, "Right")
screen.onkey(player.go_left, "Left")


#while loop to make the game keep going on and on
game_is_on = True
while game_is_on:
    time.sleep(0.05) #game speed
    screen.update() #update

    car_manager.create_car()
    car_manager.move_cars()

    #Game condition when car collision and stop the loop
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    #Keep go to the next level if player passes the level
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick() #Click to turn off screen
