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
        if count in target_stars.keys():
            prev_scope = target_stars[count]
            if distance(prev_scope, zero) > distance(scope, zero):
                target_stars[count] = scope
        else:
            target_stars[count] = scope
    target = target_stars[max(target_stars.keys())]
    return target

cords, X, Y = [], [], []
with open("_6B.txt") as f:
    for x in f:
        cord = list(map(float, x.split()))
        cords.append(cord); X.append(cord[0]); Y.append(cord[1])

plt.figure(figsize=(10,6))
plt.scatter(X, Y, alpha=0.7)
#plt.show()

claster_1, claster_2, claster_3 = [], [], []
for c in cords:
    if -7 <= c[0] <= -2 and -2.5 <= c[1] <= 2.5:
        claster_1.append(c)
    elif -2.5 <= c[0] <= 2.5 and 1.6 <= c[1] <= 6.4:
        claster_2.append(c)
    else:
        claster_3.append(c)

scope_1 = scope_target(claster_1)
scope_2 = scope_target(claster_2)
scope_3 = scope_target(claster_3)

Px = (scope_1[0]+scope_2[0]+scope_3[0])/3*10000
Py = (scope_1[1]+scope_2[1]+scope_3[1])/3*10000



print(Px, Py)