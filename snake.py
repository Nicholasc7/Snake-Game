import turtle
import time
import random


COLORS = ["orange", "olive", "brown"]
duplicates = []
ct = []
counter = 0
dupe_dir = []


win = turtle.Screen()
win.setup(width=600, height=600)
win.title("Snake!")
win.bgcolor("teal")
win.tracer(0)
turtle.listen()


snake = turtle.Turtle()
snake.shape("square")
snake.shapesize(1)
snake.color("black")
snake.speed(0)
snake.penup()
snake.setheading(0)


food = turtle.Turtle()
food.shape("square")
food.color("indigo")
food.penup()
food.shapesize(1)
food.speed(0)
food_spawns = []
for i in range(-280, 280, 20):
    food_spawns.append(i)
food.setpos(random.choice(food_spawns), random.choice(food_spawns))


def move(snake):
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


def up():
    snake.setheading(90)


def down():
    snake.setheading(270)


def right():
    snake.setheading(0)


def left():
    snake.setheading(180)


def food_move():
    snake_x = snake.xcor()
    snake_y = snake.ycor()
    food_x = food.xcor()
    food_y = food.ycor()
    if (snake_x == food_x) and (snake_y == food_y):
        food.setpos(random.choice(food_spawns), random.choice(food_spawns))
        let = "a"
        return let
    else:
        let = "b"
        return let


def snake_duplicate():
    result = food_move()
    if result == "a":
        ct.append("a")
        dupe = snake.clone()
        dupe.color(random.choice(COLORS))
        dupe.setpos(270, 280)
        dupe.speed(3)
        duplicates.append(dupe)

        snake_dir = snake.heading()
        snake_x = snake.xcor()
        snake_y = snake.ycor()
        if snake_dir == 0:
            time.sleep(1)
            duplicates[len(ct)-1].setheading(snake_dir)
            if len(duplicates) == 1:
                pos = [snake_x - 40, snake_y]
            elif len(duplicates) == 2:
                pos = [snake_x - 40, snake_y]
            elif len(duplicates) > 1:
                pos = [snake_x - 20 * len(duplicates), snake_y]
            duplicates[len(ct)-1].st()
            duplicates[len(ct)-1].color("white")
            duplicates[len(ct)-1].goto(pos[0], pos[1])


while True:
    move(snake)
    snake_dir = snake.heading()

    snake_duplicate()

    if len(duplicates) > 0:
        try:
            for i in range(len(duplicates)):
                move(duplicates[i])
        except AttributeError:
            move(duplicates[0])


        if snake_dir != dupe_dir:
            duplicates[0].setheading(snake_dir)

    turtle.onkey(up, "w")
    turtle.onkey(down, "s")
    turtle.onkey(left, "a")
    turtle.onkey(right, "d")
    win.update()
    time.sleep(.055)
win.mainloop()
