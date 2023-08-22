from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


def move_forwards():
    t.forward(10)

def move_backwards():
    t.backward(10)

def turn_left():
    new_heading = t.heading() + 10
    t.setheading(new_heading)

def turn_right():
    new_heading = t.heading() - 10
    t.setheading(new_heading)

def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

screen.listen()
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(move_forwards, "Up")
screen.onkey(move_backwards, "Down")

screen.onkey(clear, "c")
screen.exitonclick()
