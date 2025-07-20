#https://education.yandex.ru/ege/task/7954f17b-5247-4104-b3ac-b8f0d668abb2
from turtle import *
speed(1)
k = 5
up()
down()
for r in range(3):
    forward(31*k); left(90); forward(14*k); left(90)
up()
backward(4*k); right(90); forward(6*k); left(90)
down()
for r in range(3):
    forward(11*k); left(90); forward(77*k); left(90)
up()
cnt = 0
goto(0, 0)
speed(20)
for x in range(0*k,31*k,k):
    for y in range(0 * k, 15 * k, k):
        goto(x, y)
        if x < 24 * k:
            cnt += 1
            dot(2, "red")
for x in range(24*k,36*k,k):
    for y in range(-57 * k, 21 * k, k):
        goto(x, y)
        cnt += 1
        dot(2, "red")
print(cnt)
done()