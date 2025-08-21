from turtle import *
speed(10000)
k = 20
right(135)
down()
for r in range(7):
    forward(7*k); right(45); forward(8*k); right(135) #РОФЛ??????
up()
for x in range(-21*k, 11*k, k):
    for y in range(-10 * k, 1 * k, k):
        goto(x, y)
        dot(3, "red")
done()