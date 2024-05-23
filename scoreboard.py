from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-300, 470)
        self.write(arg=f"Score: {self.score}", align="center", font=("Courier", 20, "normal"))


    def plus_point(self):
        self.score += 150
        self.update_scoreboard()

    def display_final_score(self, final_score):
        self.clear()  # Clear any previous score
        self.goto(0, 0)
        self.write(f"Final Score: {final_score}", align="center", font=("Arial", 24, "normal"))
