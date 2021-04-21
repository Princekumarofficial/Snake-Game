from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

food = Food()
snake = Snake()
scoreboard = ScoreBoard()
score = 0

screen.listen()
screen.onkey(snake.move_forward, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")
screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    scoreboard.update_score()
    time.sleep(0.1)
    snake.move()

    # Collision with food
    if snake.head.distance(food) < 15:
        scoreboard.score += 1
        food.refresh()
        scoreboard.update_score()
        snake.extend_snake()

    # Colloison with wall
    if snake.head.xcor() > 290 or snake.head.ycor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290:
        high_score = score
        scoreboard.reset_sb()
        snake.reset()

    # Detect colloison with Tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            high_score = score
            scoreboard.reset_sb()

screen.exitonclick()
