#https://education.yandex.ru/ege/task/71c6e3f8-fcf1-4754-afc8-6dfc789e53cd

from turtle import *

speed(100)
k = 10

down()
for r in range(2):
    forward(14*k); left(270); backward(12*k); right(90)
up()
forward(9*k); right(90); backward(7*k); left(90)
down()
for r in range(2):
    forward(13*k); right(90); forward(6*k); right(90)
up()
for x in range(0, 30*k, k):
    for y in range(-5 * k, 20 * k, k):
        goto(x, y)
        dot(3, "red")
done()