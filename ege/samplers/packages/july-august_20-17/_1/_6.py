#https://education.yandex.ru/ege/task/b42704bc-b6b7-420b-9e9a-7b701e544087
from turtle import *
speed(10)
k = 32
down()
right(60); forward(4*k); right(120)
for r in range (4):
    forward(3*k); right(240); forward(3*k); right(120)
forward(4*k); right(90); forward((8*3**0.5)*k); right(90); forward(8*k)
up()
for x in range(-10*k, 10*k, k):
    for y in range(-20 * k, 1 * k, k):
        goto(x, y)
        dot(3, "red")
done()