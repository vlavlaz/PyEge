import numpy as np
data = []
with open("_27A.txt") as fA:
    for x in fA:
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
claster_1, claster_2 = [],[]
for x in data:
    deg.append(x[0]); r.append(x[1])
for deg, r in data:
    if 175.96 <= deg <= 195.94:
        claster_1.append([r*np.cos(np.deg2rad(deg)), r*np.sin(np.deg2rad(deg))])
    else:
        claster_2.append([r*np.cos(np.deg2rad(deg)), r*np.sin(np.deg2rad(deg))])
center_1 = find_center(claster_1)
center_2 = find_center(claster_2)
print((center_1[0]+center_2[0])/2*10000)
print((center_1[1]+center_2[1])/2*10000)


#claster1: 175.96 --> 195.94
#claster2: 322.14 --> 342.05