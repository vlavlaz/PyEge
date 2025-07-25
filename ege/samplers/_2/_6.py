#https://education.yandex.ru/ege/task/09b140f0-7fd0-42d4-b7f2-07ac9e2a5d0f
from turtle import *
k = 10
speed(10)
down()
for r in range(5):
    forward(35*k); right(90); forward(24*k); right(90)
up()
right(90); forward(7*k); right(90); forward(5*k)
down()
for r in range(4):
    right(90); forward(20*k); right(90); forward(36*k)
up()
for x in range(0*k, 35*k, k):
    for y in range(-40 * k, 9 * k, k):
        goto(x, y)
        dot(3, "red")
done()