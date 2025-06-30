#https://education.yandex.ru/ege/task/421955e0-af0d-4431-ab03-4de919832f18
from turtle import *
speed(10)
up()
goto(100, -200)
down()
left(15)
k = 30
for rep in range(7):
    left(30)
    forward(10*k)
    left(60)
up()
for x in range(-10*k, 12*k, k):
    for y in range(-10 * k, 10 * k, k):
        goto(x, y)
        dot(4, "red")
done()
#98 -> CORRECT