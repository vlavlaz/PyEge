from turtle import *
k = 20
speed(10)
up()
goto(-100, 100)
down()
for r in range(6):
    forward(7*k)
    right(120)
up()
forward(3*k)
right(90)
down()
for r in range(8):
    forward(5*k)
    right(90)
up()
for x in range(-12*k, 12*k, k):
    for y in range(-12 * k, 12 * k, k):
        goto(x, y)
        dot(3, "red")
done()
