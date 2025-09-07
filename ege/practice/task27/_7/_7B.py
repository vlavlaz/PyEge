#https://education.yandex.ru/ege/task/f47a3a69-f78a-4c45-9bcd-5cd5da9781b9

import matplotlib.pyplot as plt
def dist(A, B):
    return ((B[0] - A[0])**2+(B[1] - A[1])**2)**0.5

def anticentroid(claster):
    anti = []
    mx = 0
    for scope in claster:
        sud = 0
        for star in claster:
            sud += dist(scope, star)
        if mx < sud:
            mx = sud
            anti = scope
    return anti


cords, X, Y = [],[],[]
with open("_7B.txt") as f:
    for x in f:
        cord = list(map(float, x.split()))
        cords.append(cord); X.append(cord[0]); Y.append(cord[1])

plt.figure(figsize=(10, 6))
plt.scatter(X, Y, alpha=0.7)
plt.show()

claster_1, claster_2, claster_3 = [], [], []

for c in cords:
    if 8 < c[0] < 16 and 8 < c[1] < 16:
        claster_1.append(c)
    elif 26 < c[0] < 34 and 26 < c[1] < 34:
        claster_2.append(c)
    elif 54 < c[0] < 62 and 4 < c[1] < 12:
        claster_3.append(c)

anti_1 = anticentroid(claster_1)
anti_2 = anticentroid(claster_2)
anti_3 = anticentroid(claster_3)

Px = (anti_1[0]+anti_2[0]+anti_3[0])/3*10000
Py = (anti_1[1]+anti_2[1]+anti_3[1])/3*10000

print(Px, Py)