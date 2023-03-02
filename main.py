from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('my snake2 game')
screen.tracer(0)

score=Score()
food= Food()
snake= Snake()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(snake.speed)
    snake.move()


    #detect collision with food
    if snake.head.distance(food)<19:
        food.regenerate()
        score.increasescore()
        snake.extend()
        time.sleep(snake.increase_speed())

    #detect collision with wall
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290 :
        game_is_on=False
        score.game_over()

    #detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()



screen.exitonclick()
