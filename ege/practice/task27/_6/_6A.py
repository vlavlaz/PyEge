#https://education.yandex.ru/ege/task/bedd784e-caf0-4568-8016-aacf56fe903d

import matplotlib.pyplot as plt

def distance(A, B):
    return ((B[0]-A[0])**2+(B[1]-A[1])**2)**0.5
def scope_target(claster):
    target_stars = {}
    zero = [0, 0]
    for scope in claster:
        count = 0
        for star in claster:
            if distance(scope, star) <= 2.1:
                count+=1
        target_stars[count] = scope
    mx = max(target_stars.keys())
    mn_dist = 999999999
    target = []
    for s, t in target_stars.items():
        if s == mx:
            d = distance(zero, t)
            if d < mn_dist:
                target = t
                mn_dist = d
    return target

cords, X, Y = [], [], []
with open("_6A.txt") as f:
    for x in f:
        cord = list(map(float, x.split()))
        cords.append(cord); X.append(cord[0]); Y.append(cord[1])
plt.figure(figsize=(10,6))
plt.scatter(X, Y, alpha=0.7)
#plt.show()
clater_1, clater_2 = [], []
for c in cords:
    if -47< c[0] < -40 and -28 < c[1] < -22:
        clater_1.append(c)
    else:
        clater_2.append(c)

scope_1 = scope_target(clater_1)
scope_2 = scope_target(clater_2)

Px = (scope_1[0]+scope_2[0])/2*10000
Py = (scope_1[1]+scope_2[1])/2*10000

print(Px, Py)