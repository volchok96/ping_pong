from turtle import Turtle
UP = 90
DOWN = 270
MOVE_DISTANCE = 20

class Pad(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def up(self):
        if -275 < self.ycor() < 275:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def down(self):
        if -275 < self.ycor() < 275:
            new_y = self.ycor() - MOVE_DISTANCE
            self.goto(self.xcor(), new_y)





