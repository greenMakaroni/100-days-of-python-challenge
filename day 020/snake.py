# Classic snake game challenge
from turtle import Turtle
starting_positions=[(0, 0), (-20, 0), (-40, 0)]

class Snake:

    def __init__(self):
        self.snakeLength = 3
        self.segments = []
        self.xpos = 0
        self.ypos = 0
        self.draw_snek()

    def draw_snek(self):
        for position in starting_positions:
            segment = Turtle("square")
            segment.penup()
            segment.color("white")
            segment.goto(position)
            self.segments.append(segment)

            self.xpos -= 20
            self.segments.append(segment)

    def move(self):
        for segment_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_number - 1].xcor()
            new_y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(new_x, new_y)
        self.segments[0].forward(20)

    def turn_right(self):
        self.segments[0].right(90)

    def turn_left(self):
        self.segments[0].left(90)

