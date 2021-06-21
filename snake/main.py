from turtle import Turtle, Screen

screen = Screen()
screen.tracer(0)
initial_pos = [(0, 0), (-20, 0), (-40, 0)]
actual_pos = []
start_game = True


def setup_screen():
    screen.setup(width=500, height=450)
    screen.bgcolor('black')
    

def setup_snake(pos):
    segment = Turtle()
    segment.shape('square')
    segment.color('white')
    segment.penup()
    segment.goto(pos)
    actual_pos.append(segment)

def main():
    for index, num in enumerate(initial_pos):
        setup_snake(initial_pos[index])
        setup_screen()
    
    while start_game:
        for seg in actual_pos:
            seg.forward(20)
            screen.update()
    screen.exitonclick()

if __name__ == '__main__':
    main()