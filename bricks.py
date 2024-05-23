from turtle import Turtle
import random

class Brick(Turtle):
    def __init__(self, x, y, color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.goto(x, y)


class BrickManager:
    def __init__(self):
        self.bricks = []
        self.create_bricks()

    def create_bricks(self):
        start_x = -350
        start_y = 450
        brick_width = 80
        brick_height = 30
        rows = 5
        columns = 9
        row_colors = ["red", "green", "blue", "purple", "yellow"]

        for row in range(rows):
            for col in range(columns):
                x = start_x + col * brick_width
                y = start_y - row * brick_height
                brick = Brick(x, y, row_colors[row])
                self.bricks.append(brick)