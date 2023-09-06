from turtle import Turtle

#Font style
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__() #Call the constructor of class
        self.level = 1 #Start from level 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()

    #Update the scoreboard
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    #Level up and save the scoreboard
    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    #Display "game over" on screen
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
