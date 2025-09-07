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

def max_dist(c, claster):
    mx = 0
    for star in claster:
        d = dist(c, star)
        if d > mx:
            mx = d
    return mx

cords, X, Y = [], [], []
with open("_27_B.txt") as f:
    for l in f:
        l = l.replace(",", ".")
        cord = list(map(float, l.split()))
        cords.append(cord), X.append(cord[0]), Y.append(cord[1])
#plt.figure(figsize=(10,6))
#plt.scatter(X, Y, alpha=0.7)
#plt.show()
claster_mx, claster_mn, claster = [], [], []
for c in cords:
    if 8 < c[0] < 15 and 12<c[1]<18:
        claster_mx.append(c)
    elif 19 < c[0] < 24 and 23 < c[1] < 27:
        claster_mn.append(c)
    elif 13 < c[0] < 17 and 21 < c[1] < 26:
        claster.append(c)
cmx = centorid(claster_mx)
cmn = centorid(claster_mn)
cmid = centorid(claster)
Q1 = dist(cmx, cmn)*10000
Q2 = max(max_dist(cmx, claster_mx), max_dist(cmn, claster_mn), max_dist(cmid, claster))*10000
print(Q1, Q2)