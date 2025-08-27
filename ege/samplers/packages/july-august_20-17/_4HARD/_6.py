from turtle import *
speed(10)
k = 10
for r in range(7):
    right(90); forward(7*k); right(90); forward(6*k)
up()
right(90); forward(3*k); right(90); forward(k)
down()
for r in range(4):
    right(90); forward(6*k); right(90); forward(11*k)
up()
for x in range(0, -21*k, -k):
    for y in range(0, -11 * k, -k):
        goto(x, y)
        dot(3, "red")
done()

