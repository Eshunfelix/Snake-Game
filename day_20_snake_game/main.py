from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
pos = [(0, 0), (-20, 0), (-40, 0)]
segs = []

snake = Snake()
snake.create_snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
food = Food()
score = Score()



gaming = True
while gaming:

    screen.update()
    time.sleep(0.1)
    snake.move()


    if snake.segs[0].distance(food) < 15:
        food.refresh()
        #Food.refresh(food) another way of calling the refresh method on
        # the food object. the food object is clearly passed as the self.
        score.increase_score() #Score.increase_score(score)
        snake.add_segments()   # Score.add_segment(snake)
        print(snake.currentpos)

    # Detect Wall collision
    if snake.segs[0].xcor() > 280 or snake.segs[0].xcor() < -280 \
            or snake.segs[0].ycor() < -280 or snake.segs[0].ycor() > 280:
        score.game_over() #Score.gama_over(score)
        gaming = False

    for i in snake.segs[1:]:
        if snake.segs[0].distance(i) < 10:
            score.game_over()
            #Score.game_over(score)
            gaming = False

screen.exitonclick()

