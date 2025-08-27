#https://education.yandex.ru/ege/task/d21010ca-1bc2-4a0e-b0d3-cc3fa3f07929

from turtle import *
speed(10)
up()
goto(0, 0)
k = 10
down()
for r in range(3):
    forward(5*k); right(90); forward(12*k); right(90)
up()
forward(3*k); right(90); forward(2*k); right(90)
down()
for r in range(4):
    forward(5*k); right(90); forward(12*k)
up()
for x in range(-10*k, 20*k, k):
    for y in range(-30 * k, 4 * k, k):
        goto(x,y)
        dot(3, "red")
done()