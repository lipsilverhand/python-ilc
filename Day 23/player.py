from turtle import Turtle

STARTING_POSITION = (0, -280) #The player starting on the bottom screen
MOVE_DISTANCE = 10 #Each step distance
FINISH_LINE_Y = 280 #Finish line


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    #Move the player upwards
    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    #Check player reach the line
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
