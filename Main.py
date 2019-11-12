import turtle
import time
import random


delay = 0.1

score = 0
high_score = 0

segments = []

# setup the screen
Window = turtle.Screen()
Window.title("Snake by #Paint")
Window.bgcolor("green")
Window.setup(width=600, height=600)
Window.tracer(0) # turn off the screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("red")
head.penup()
head.goto(0,0)
head.direction = "stop"

# food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("purple")
food.penup()
food.goto(0,100)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))


# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    
    if head.direction == "down":
        head.sety(head.ycor() - 20)

    if head.direction == "left":
        head.setx(head.xcor() - 20)
    
    if head.direction == "right":
        head.setx(head.xcor() + 20)

# key bindings
Window.listen()
Window.onkeypress(go_up, "w")
Window.onkeypress(go_down, "s")
Window.onkeypress(go_left, "a")
Window.onkeypress(go_right, "d")

# Main game loop
while True:
    Window.update()

    # Colision with border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Hide segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the segments list
        segments.clear()

        delay = 0.1

        score = 0

        pen.clear()
        pen.write("Score: {}   High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # food colision
    if head.distance(food) < 20:
        # Move food to random spot
        food.goto(random.randrange(-280, 280, 20), random.randrange(-280, 280, 20))

        # add segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("black")
        new_segment.penup()
        segments.append(new_segment)
        
        delay -= 0.001

        score+=10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}   High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Move the end segment first in reverse
    for index in range(len(segments)-1, 0, -1):
        segments[index].goto(segments[index-1].xcor(), segments[index-1].ycor())

    # Move segment 0 to the head
    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # Body colision
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # Hide segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            delay = 0.1

            score = 0

            pen.clear()
            pen.write("Score: {}   High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))


    time.sleep(delay)

Window.mainloop()