#https://education.yandex.ru/ege/task/5d8ac905-5349-459b-8922-908a0927d6e1
from turtle import *
right(45)
speed(10)
k = 40
up()
goto(-100, 300)
down()

for r in range(7):
    forward(6*k)
    right(45)
    forward(12*k)
    right(135)
up()

for x in range(-10*k, 10*k, k):
    for y in range(-10 * k, 10 * k, k):
        goto(x,y)
        dot(4, "red")
done()

#44 -> CORRECT
#https://education.yandex.ru/ege/task/3bab2754-282f-4c53-8edc-ac3e702d2392 == ЧТОНАХУЙ