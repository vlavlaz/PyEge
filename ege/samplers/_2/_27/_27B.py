import numpy as np
data = []
with open("_27B.txt") as fB:
    for x in fB:
        d = x.split()
        for i in range(2):
            d[i] = float(d[i])
        data.append(d)

def distance(x1, y1, x2, y2):
    return ((x2-x1)**2+(y1-y2)**2)**0.5
def find_center(claster):
    cx, cy = 0, 0
    minsud = 99999999999
    for x1, y1 in claster:
        sud = 0
        for x2, y2 in claster:
            sud += distance(x1, y1, x2, y2)
        if minsud > sud:
            minsud = sud
            cx, cy = x1, y1
    return [cx, cy]
deg, r = [], []
claster_1, claster_2, claster_3 = [],[],[]
for x in data:
    deg.append(x[0]); r.append(x[1])
print(sorted(deg))
#claster1: 33.15 --> 53.14
#claster2: 72.52 --> 92.49
#claster3: 156.11 --> 176.11

for deg, r in data:
    if 33.15 <= deg <= 53.14:
        claster_1.append([r*np.cos(deg), r*np.sin(deg)])
    elif 72.52 <= deg <= 92.49:
        claster_2.append([r*np.cos(deg), r*np.sin(deg)])
    else:
        claster_3.append([r*np.cos(deg), r*np.sin(deg)])
center_1 = find_center(claster_1)
center_2 = find_center(claster_2)
center_3 = find_center(claster_3)

print((center_1[0]+center_2[0]+center_3[0])/3*10000)
print((center_1[1]+center_2[1]+center_3[1])/3*10000)
