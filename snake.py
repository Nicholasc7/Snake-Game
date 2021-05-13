# TODO: Add movement functionality to duplicates.
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


grid_positions_x = []
grid_positions_y = []
for num in range(-280, 280, 20):
    grid_positions_x.append(num)
    grid_positions_y.append(num)


def grid():
    vertical_lines = []
    horizontal_lines = []
    for line in range(len(grid_positions_x)):
        i = turtle.Turtle()
        vertical_lines.append(i)
        horizontal_lines.append(i)

    for i in range(len(grid_positions_x)):
        vertical_lines[i].speed(0)
        vertical_lines[i].ht()
        vertical_lines[i].penup()
        vertical_lines[i].setpos(grid_positions_x[i] + 10, 270)
        vertical_lines[i].setheading(270)
        vertical_lines[i].color("white")
        vertical_lines[i].pendown()
        vertical_lines[i].forward(540)

    for i in range(len(grid_positions_x)):
        horizontal_lines[i].speed(0)
        horizontal_lines[i].ht()
        horizontal_lines[i].penup()
        horizontal_lines[i].setpos(-270, grid_positions_y[i] + 10)
        horizontal_lines[i].setheading(0)
        horizontal_lines[i].color("white")
        horizontal_lines[i].pendown()
        horizontal_lines[i].forward(540)


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

    # If there is a collision, create a head clone. Set hidden. Append to list of duplicates.
    if result == "a":
        ct.append("a")
        dupe = snake.clone()
        dupe.ht()
        dupe.color(random.choice(COLORS))
        dupe.speed(0)
        dupe.setpos(270, 270)
        duplicates.append(dupe)

        # Grab the Previous head's position and heading information.
        snake_dir = snake.heading()
        snake_x = snake.xcor()
        snake_y = snake.ycor()

        # Move the clone to the back of the line
        if snake_dir == 0:
            time.sleep(.25)
            duplicates[len(ct)-1].setheading(snake_dir)
            pos = [snake_x - (20 * len(duplicates)), snake_y]
            duplicates[len(ct)-1].st()
            duplicates[len(ct)-1].goto(pos[0], pos[1])
            win.update()
            time.sleep(.25)

        if snake_dir == 90:
            time.sleep(.25)
            duplicates[len(ct)-1].setheading(snake_dir)
            pos = [snake_x, snake_y - (20 * len(duplicates))]
            duplicates[len(ct)-1].st()
            duplicates[len(ct)-1].goto(pos[0], pos[1])
            win.update()
            time.sleep(.25)

        if snake_dir == 180:
            time.sleep(.25)
            duplicates[len(ct)-1].setheading(snake_dir)
            pos = [snake_x + (20 * len(duplicates)), snake_y]
            duplicates[len(ct)-1].st()
            duplicates[len(ct)-1].goto(pos[0], pos[1])
            win.update()
            time.sleep(.25)

        if snake_dir == 270:
            time.sleep(.25)
            duplicates[len(ct)-1].setheading(snake_dir)
            pos = [snake_x, snake_y + 20 * len(duplicates)]
            duplicates[len(ct)-1].st()
            duplicates[len(ct)-1].goto(pos[0], pos[1])
            win.update()
            time.sleep(.25)


def movement():
    turtle.onkey(up, "w")
    turtle.onkey(down, "s")
    turtle.onkey(left, "a")
    turtle.onkey(right, "d")
    move(snake)
    if len(duplicates) > 0:
        for i in range(len(duplicates)):
            move(duplicates[0])
            snake_dir = snake.heading()
            duplicates[0].setheading(snake_dir)

    win.update()





grid()
while True:
    movement()

    turtle.onkey(up, "w")
    turtle.onkey(down, "s")
    turtle.onkey(left, "a")
    turtle.onkey(right, "d")
    snake_dir = snake.heading()

    snake_duplicate()

    time.sleep(.055)
win.mainloop()
