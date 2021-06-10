#pip install turtle
#https://docs.python.org/3/library/turtle.html
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title='bet the turtle', prompt='Enter a color')

tim = Turtle(shape='turtle')
tim.penup()
tim.goto(x=-240, y=0)

tom = Turtle(shape='turtle')
tom.penup()
tom.goto(x=-240, y=25)

ten = Turtle(shape='turtle')
ten.penup()
ten.goto(x=-240, y=-25)

screen.exitonclick()