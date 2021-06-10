#pip install turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

while True:
    screen.onkey(key='space', fun=move_forwards)
    screen.onkey(lambda: tim.setheading(90), 'Up')
    screen.onkey(lambda: tim.setheading(180), 'Left')
    screen.onkey(lambda: tim.setheading(0), 'Right')
    screen.onkey(lambda: tim.setheading(270), 'Down')
    screen.listen()
    screen.exitonclick()