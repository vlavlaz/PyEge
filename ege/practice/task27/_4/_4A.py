#https://education.yandex.ru/ege/task/c1873d15-dca4-413b-955d-5888db94cec1

import pandas as pd
import matplotlib.pyplot as plt
def distance(A,B):
    return ((B[0]-A[0])**2+(B[1]-A[1])**2)**0.5
def find_centroid(claster):
    mn = 9999999999
    centroid = []
    for mb_center in claster:
        sud = 0
        for cord in claster:
            sud += distance(mb_center, cord)
        if sud < mn:
            mn = sud
            centroid = mb_center
    return centroid


cords, X, Y = [], [], []
with open("_4A.txt") as f:
    for x in f:
        x = x.replace(",", ".")
        cord = list(map(float, x.split()))
        cords.append(cord)
        X.append(cord[0]); Y.append(cord[1])

#data = {
#    "X": X,
#    "Y": Y
#}
#df = pd.DataFrame(data)
#plt.figure(figsize=(10, 6))
#plt.scatter(df["X"], df["Y"], alpha=0.7)
#plt.show()

claster_1, claster_2 = [],[]
for cord in cords:
    if -7 < cord[0] < 0 and -8.7 < cord[1] < 2.8:
        claster_1.append(cord)
    else:
        claster_2.append(cord)
centroid_1 = find_centroid(claster_1)
centroid_2 = find_centroid(claster_2)
Px = (centroid_1[0]+centroid_2[0])/2*10000
Py = (centroid_1[1]+centroid_2[1])/2*10000
print(Px, Py)