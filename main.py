from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from bricks import BrickManager
from scoreboard import Scoreboard
import time


#------------SCREEN-----------#
screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=1000)
screen.title("BreakOut")



#----------BALL And Paddle---------#
ball = Ball(0, 0)
ball.hideturtle()
ball.goto(0, -350)
ball.showturtle()
paddle = Paddle(0, -450)


#------------Player Movement------------#
screen.listen()
screen.onkey(paddle.right, "Right")
screen.onkey(paddle.left, "Left")



#------------ScoreBoard--------------#
scoreboard = Scoreboard()


#-----------Bricks---------------------#
brick_manager = BrickManager()



#---------Game Manager----------#
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() < -460:  # If ball goes below this y-coordinate, end the game
        game_is_on = False
        scoreboard.display_final_score(scoreboard.score)

    #Collision with walls
    if ball.xcor() > 370:
        ball.bounce_left()
    if ball.xcor() < -370:
        ball.bounce_left()
    if ball.ycor() > 460:
        ball.bounce_y()

    #Collision with Paddle
    if ball.distance(paddle) < 50:
        print("yes")
        ball.bounce_y()

    #collision with bricks
    for brick in brick_manager.bricks:
        if ball.distance(brick) < 50:
            brick_manager.bricks.remove(brick)
            brick.hideturtle()
            scoreboard.plus_point()

            # Check where the ball hit the brick
            if abs(ball.xcor() - brick.xcor()) < 40:
                ball.bounce_y()
            else:
                ball.bounce_left()

screen.exitonclick()




# Create a screen to put the game in
# Create a board you can move left and right , set bounderies for the wall (Padding)
# Create the ball, the ball should interact with the peddal, the sides of the screen, the top of the screen and with the
#bricks. the location the ball hits the bricks should matter
#Create the bricks and have them interact with the ball, bricks can have different colors.
# game over state if the ball hits the bottom of the screen
# a scoring system to keep score