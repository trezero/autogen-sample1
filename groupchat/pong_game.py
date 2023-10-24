# filename: pong_game.py

import turtle

# Create the screen
sc = turtle.Screen()
sc.title("Pong Game")
sc.bgcolor("white")

# Left paddle
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("black")
left_pad.shapesize(stretch_wid=6, stretch_len=1)
left_pad.penup()
left_pad.goto(-350, 0)

# Right paddle
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("black")
right_pad.shapesize(stretch_wid=6, stretch_len=1)
right_pad.penup()
right_pad.goto(350, 0)

# Ball of circle shape
ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 6    # increased by 20%
ball.dy = -6   # increased by 20%

# Display the score
score = turtle.Turtle()
score.speed(0)
score.color("black")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Left : 0    Right: 0",
            align="center",
            font=("Courier", 24, "normal"))


# Moving the left paddle
def paddleaup():
    y = left_pad.ycor()
    y += 24  # increased by 20%
    left_pad.sety(y)

def paddleadown():
    y = left_pad.ycor()
    y -= 24  # increased by 20%
    left_pad.sety(y)

# Moving the right paddle
def paddlebup():
    y = right_pad.ycor()
    y += 24  # increased by 20%
    right_pad.sety(y)

def paddlebdown():
    y = right_pad.ycor()
    y -= 24  # increased by 20%
    right_pad.sety(y)

# Keyboard bindings
sc.listen()
sc.onkeypress(paddleaup, "w")
sc.onkeypress(paddleadown, "s")
sc.onkeypress(paddlebup, "Up")
sc.onkeypress(paddlebdown, "Down")

def ball_move():
    ball.dx = ball.dx
    ball.dy = ball.dy
    ball.goto(ball.xcor() + ball.dx, ball.ycor() + ball.dy)
    # Border collision
    if ball.ycor() >= 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() <= -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() >= 390:
        ball.goto(0, 0)
        ball.dy *= -1

    if ball.xcor() <= -390:
        ball.goto(0, 0)
        ball.dy *= -1
    
    # Ball and paddle collision logic
    if ((350 > ball.dx > 0) and
            (right_pad.ycor() + 50 > ball.ycor() > right_pad.ycor() - 50)):
        ball.color("blue")
        ball.dx *= -1

    elif ((ball.dx < 0) and
          (-350 < ball.dx < 0) and
          (left_pad.ycor() + 50 > ball.ycor() > left_pad.ycor() - 50)):
        ball.color("red")
        ball.dx *= -1
    sc.ontimer(ball_move, 20)

# call the function to move the ball
sc.ontimer(ball_move, 20)

# Infinite loop
turtle.mainloop()