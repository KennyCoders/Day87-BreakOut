from turtle import Turtle

STARTING_POSITION = (0, -400)


class Paddle(Turtle,):
    def __init__(self, x, y):
        super().__init__()
        self.create_paddle()
        self.penup()
        self.right()
        self.left()
        self.penup()
        self.goto(x, y)


    def create_paddle(self,):
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.setheading(0)
        self.shapesize(stretch_wid=1, stretch_len=5)

    def right(self):
        new_x = self.xcor() + 40
        self.goto(new_x, self.ycor())

    def left(self):
        new_x = self.xcor() - 40
        self.goto(new_x, self.ycor())