#https://education.yandex.ru/ege/task/3d1c2b6c-075c-467b-b1ae-b9443f968900
from turtle import *
speed(10)
up()
goto(-50, 50)
k = 10
right(30); forward(4*k); right(330)
down()
forward(4*k); right(90); forward(7*k); right(45); forward(32**0.5*k)
right(135); forward(11*k)
up()
for x in range(-10*k, 10*k, k):
    for y in range(-10 * k, 10 * k, k):
        goto(x,y)
        dot(3, "red")
done()