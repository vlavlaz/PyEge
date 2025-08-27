from turtle import *
speed(10)
k = 20
for r in range (8):
    right(60); forward(7*k); right(60)
up()
cnt = 0
for x in range(-4*k, 4*k, k):
    for y in range(-8*k, 1 * k, k):
        goto(x, y)
        if ((y < (3**0.5)*x and -7/2*k <= x <= 0)  or
            (y < (-3**0.5)*x and 0<x<=7/2*k)) and y > -7*(3**0.5)*k/2:
            dot(3, "red")
            cnt+=1
print(cnt)
done()