### Create a Pong game with Turtle Module from Python


from turtle import Turtle, Screen

from ball import Ball
from bar import Bar
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

#ball.py
#from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1


    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()

#bar.py
#from turtle import Turtle

class Bar(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def goUp(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def goDown(self):
        self.goto(self.xcor(), self.ycor() - 20)
#scoreboard.py
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.updateScoreboard()

    def updateScoreboard(self):
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.updateScoreboard()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.updateScoreboard()

right_bar = Bar((350,0))
left_bar = Bar((-350,0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(right_bar.goUp,"Up")
screen.onkey(right_bar.goDown,"Down")

screen.onkey(left_bar.goUp,"w")
screen.onkey(left_bar.goDown,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with upper and lower wall
    if ball.ycor() > 280 or ball.ycor() < - 280:
        ball.bounce_y()

    # detect collision with bar
    if ball.distance(right_bar) < 50 and ball.xcor() > 320 or ball.distance(left_bar) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect when a right bar misses the ball
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()

    # detect when a left bar misses the ball
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()
screen.exitonclick()
