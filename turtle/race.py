#pip install turtle
#https://docs.python.org/3/library/turtle.html
from turtle import Turtle, Screen
import random

is_race = False

screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title='bet the turtle', prompt='Enter a color')
pos = [-25, 0, 25]
colors = ['red', 'blue', 'yellow']
created_turtle = []
winner = ''


for turt in range(0, 3):
    instance = Turtle(shape='turtle')
    instance.penup()
    instance.color(colors[turt])
    instance.goto(x=-240, y=pos[turt])
    created_turtle.append(instance)


if bet:
    is_race = True

while is_race:
    for turtle in created_turtle:
        if int(round(turtle.xcor(), 5)) > 230:
            winner = turtle.pencolor()
            is_race = False

        rand = random.randint(0, 10)
        turtle.forward(rand)
        

print('winner ' + winner)
        

screen.exitonclick()