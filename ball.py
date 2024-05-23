from turtle import Turtle
import time
class Ball(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(x, y)
        self.x_move = 5
        self.y_move = 10
        self.speed("fastest")
        self.move_speed = 0.000001
        self.bounce_left()
        self.bounce_right()
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_left(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def bounce_right(self):
        self.x_move *= 1
        self.move_speed *= 0.9
    def bounce_y(self):
        self.y_move *= -1



