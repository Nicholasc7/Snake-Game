import turtle
import time


win = turtle.Screen()
win.setup(width=600, height=600)
win.title("Snake!")
win.bgcolor("dark grey")
win.tracer(0)


snake = turtle.Turtle()
snake.shape("square")
snake.shapesize(1)
snake.color("black")
snake.speed(0)
snake.penup()
snake.setheading(180)


def move():
    direction = snake.heading()
    if direction == 90:
        ypos = snake.ycor()
        snake.sety(ypos + 20)

    if direction == 0:
        xpos = snake.xcor()
        snake.setx(xpos + 20)

    if direction == 180:
        xpos = snake.xcor()
        snake.setx(xpos - 20)

    if direction == 270:
        ypos = snake.ycor()
        snake.sety(ypos - 20)


while True:
    move()
    win.update()
    time.sleep(.25)



win.mainloop()
