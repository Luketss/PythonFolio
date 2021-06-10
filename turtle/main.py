#pip install turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.setheading(90)
    tim.forward(10)

def move_backwards():
    tim.setheading(270)
    tim.forward(10)

def move_left():
    tim.setheading(180)
    tim.forward(10)

def move_right():
    tim.setheading(0)
    tim.forward(10)

while True:
    screen.listen()
    screen.onkey(lambda: move_forwards(), 'Up')
    screen.onkey(lambda: move_backwards(), 'Down')
    screen.onkey(lambda: move_left(), 'Left')
    screen.onkey(lambda: move_right(), 'Right')

    screen.exitonclick()