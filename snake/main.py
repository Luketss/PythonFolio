from turtle import Turtle, Screen

screen = Screen()
snake_len = 3
initial_pos = [(0, 0), (-20, 0), (-40, 0)]

def setup_screen():
    screen.setup(width=500, height=450)
    screen.bgcolor('black')

def setup_snake(snake, pos):
    snake.shape('square')
    snake.color('white')
    snake.goto(pos)

def main():
    for num in range(0, snake_len):
        snake = Turtle()
        setup_snake(snake, initial_pos[num])
        setup_screen()
    screen.exitonclick()

if __name__ == '__main__':
    main()