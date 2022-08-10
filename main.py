from turtle import Turtle, Screen, colormode
from random import randint

blocks = []


def pack_blocks():
    for x_position in range(-350, 380, 100):
        for y_position in range(120, 260, 20):
            colormode(255)
            r = randint(0, 255)
            b = randint(0, 255)
            g = randint(0, 255)
            block = Turtle()
            block.shape("square")
            block.penup()
            block.shapesize(stretch_wid=1, stretch_len=5)
            block.color(r, b, g)
            block.goto(x_position, y_position)
            blocks.append(block)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=8, stretch_wid=1)
        self.penup()
        self.color("white")
        self.goto(0, -200)
        self.speed("fastest")

    def go_left(self):
        self.setheading(0)
        self.forward(10)
        screen.update()

    def go_right(self):
        self.setheading(180)
        self.forward(30)
        screen.update()


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")

        self.x_move = 2
        self.y_move = 2


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 260)
        self.write(self.score, align="center", font=("Courier", 20, "normal"))


    def scored(self):
        self.score += 1
        self.update_scoreboard()


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("BREAKOUT GAME")
screen.tracer(0)

pack_blocks()
player = Player()
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.go_right, "Left")
screen.onkeypress(player.go_left, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    if ball.ycor() > 260:
        ball.bounce_y()

    if ball.ycor() < -280:
        ball.reset_position()
        game_is_on = False

    if ball.xcor() > 380:
        ball.bounce_x()

    if ball.xcor() < -380:
        ball.bounce_x()

    if ball.distance(player) < 100 and ball.ycor() == -180:
        ball.bounce_y()

    for each_block in blocks:
        if ball.distance(each_block) < 20:
            each_block.hideturtle()
            each_block = 0
            ball.bounce_y()
            scoreboard.scored()


screen.exitonclick()

