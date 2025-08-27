#https://education.yandex.ru/ege/task/2f467dd3-1756-4d10-8c51-77be996e3c08
from turtle import *
k = 5
up()
goto(-100,200)
speed(50)
forward(10*k)
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
for x in range(20*k, 80*k, k):
    for y in range(-30*k, 10*k, k):
        goto(x, y)
        dot(3, "red")
done()