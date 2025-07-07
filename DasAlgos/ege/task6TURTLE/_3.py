#https://education.yandex.ru/ege/task/2f467dd3-1756-4d10-8c51-77be996e3c08
#WRONG
from turtle import *
k = 5
up()
goto(-100,100)
speed(50)
forward(10)
down()
for i in range(6):
    forward(50*k)
    right(90)
    forward(43*k)
    right(90)
up()
forward(40*k)
right(90*k)
forward(40*k)
down()
for i in range(9):
    forward(40*k)
    left(90)
    forward(20*k)
    left(90)
up()
for x in range(10*k, 60*k, 10):
    for y in range(-60*k, -10*k, 10):
        goto(x, y)
        dot(4, "red")
done()