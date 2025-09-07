#https://education.yandex.ru/ege/task/7f847262-1f0a-40f6-ae63-310d04bf277a
import matplotlib.pyplot as plt
def dist(A, B):
    return ((B[0]-A[0])**2+(B[1]-A[1])**2)**0.5

def centorid(claster):
    center = []
    mn = 99999999
    for scope in claster:
        sud = 0
        for star in claster:
            sud += dist(scope, star)
        if mn > sud:
            mn = sud
            center = scope
    return center

cords, X, Y = [], [], []
with open("_27_A.txt") as f:
    for l in f:
        l = l.replace(",", ".")
        cord = list(map(float, l.split()))
        cords.append(cord), X.append(cord[0]), Y.append(cord[1])
plt.figure(figsize=(10,6))
plt.scatter(X, Y, alpha=0.7)
#plt.show()
claster_1, claster_2 = [], []
for c in cords:
    if 1 < c[0] < 6 and 5<c[1]<8:
        claster_1.append(c)
    else:
        claster_2.append(c)
c_1 = centorid(claster_1)
c_2 = centorid(claster_2)
Px = min(c_1[0], c_2[0])*10000
Py = min(c_1[1], c_2[1])*10000
print(Px, Py)