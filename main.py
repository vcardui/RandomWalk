import random
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("aquamarine3")
tim.speed(10)

tim.penup()
tim.setposition(0,0)
tim.pensize(width=10)
tim.pendown()

for i in range(0,500):
    color = "#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
    tim.color(color)

    random_choice = random.randint(0,4)

    if random_choice == 0:
        tim.forward(20)
    elif random_choice == 1:
        tim.right(90)
        tim.forward(20)
    elif random_choice == 2:
        tim.left(90)
        tim.forward(20)
    elif random_choice == 3:
        tim.left(180)
        tim.forward(20)


screen = Screen()
screen.exitonclick()