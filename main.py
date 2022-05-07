import turtle 
import random
import time
points=0
delay=0.1
oldfruit=[]
screen=turtle.Screen()
screen.title('Snake Game')
screen.setup(width=700, height=700)
screen.tracer(0)
turtle.bgcolor('orange')
turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310,250)
turtle.pendown()
turtle.color('black')
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()
snake=turtle.Turtle()
snake.speed(0)
snake.color('black')
snake.shape('square')
snake.penup()
snake.goto(0,0)
snake.direction='stop'
fruit=turtle.Turtle()
fruit.speed(0)
fruit.color('red')
fruit.shape('circle')
fruit.penup()
fruit.goto(50,50)
score=turtle.Turtle()
score.speed(0)
score.color('blue')
score.penup()
score.goto(20,300)
score.hideturtle()
score.write('Score: ', align='center', font=('courier',24,"bold"))
def snake_go_up():
    if snake.direction!= "down":
        snake.direction="up"
def snake_go_down():
    if snake.direction!="up":
        snake.direction="down"
def snake_go_right():
    if snake.direction!="left":
        snake.direction="right"
def snake_go_left():
    if snake.direction!="right":
        snake.direction="left"
def snake_move():
    if snake.direction=="up":
        y=snake.ycor()
        snake.sety(y+20)
    if snake.direction=="down":
        y=snake.ycor()
        snake.sety(y-20)
    if snake.direction=="left":
        x=snake.xcor()
        snake.setx(x-20)
    if snake.direction=="right":
        x=snake.xcor()
        snake.setx(x+20)
screen.listen()
screen.onkeypress(snake_go_up,"Up")
screen.onkeypress(snake_go_down,"Down")
screen.onkeypress(snake_go_left,"Left")
screen.onkeypress(snake_go_right,"Right")
while True:
    screen.update()
    if (snake.distance(fruit)<20):
        x=random.randint(-290, 270)
        y=random.randint(-240, 240)
        fruit.goto(x,y)
        score.clear()
        points+=1
        score.write("Score: {}".format(points), align="center", font=("courier",24, "bold"))
        delay-=0.001
        new_fruit=turtle.Turtle()
        new_fruit.speed(0)
        new_fruit.shape("square")
        new_fruit.color("red")
        new_fruit.penup()
        oldfruit.append(new_fruit)
    for index in range (len(oldfruit)-1, 0, -1):
        a=oldfruit[index-1].xcor()
        b=oldfruit[index-1].ycor()
        oldfruit[index].goto(a,b)
    if len(oldfruit) > 0:
        a=snake.xcor()
        b=snake.ycor()
        oldfruit[0].goto(a,b)
    snake_move()
    if snake.xcor()>280 or snake.xcor()<-290 or snake.ycor()>240 or snake.ycor()<-240:
        time.sleep(1)
        screen.clear()
        screen.bgcolor('orange')
        score.goto(0,0)
        score.write("Game Over \n Your Score is: {}".format(points), align="center", font=("courier",24, "bold"))
    for food in oldfruit:
        if food.distance(snake)<20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor('orange')
            score.goto(0,0)
            score.write("Game Over \n Your Score is: {}".format(points), align="center", font=("courier",24, "bold"))
    time.sleep(delay)
turtle.Terminator()