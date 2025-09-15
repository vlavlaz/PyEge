import matplotlib.pyplot as plt
def dist(A, B):
    return ((A[0]-B[0])**2+(A[1]-B[1])**2)**0.5
data, X, Y = [],[],[]
def centroid(claster):
    c = []
    mn = 9999999999
    for center in claster:
        su = 0
        for star in claster:
            su += dist(star, center)
        if su < mn:
            mn = su
            c = center
    return c

with open("_A.txt") as f:
    for l1 in f:
        l = l1.replace(",", ".")
        d = list(map(float, l.split()))
        data.append(d)
        X.append(d[0]); Y.append(d[1])
#plt.figure(figsize=(10, 6))
#plt.scatter(X, Y, alpha=0.7)
#plt.show()
cl_1, cl_2 = [], []
for x, y in data:
    if 4 <= x <= 16 and -30 <= y <= 0:
        cl_1.append([x,y])
    else:
        cl_2.append([x,y])
center_1, center_2 = centroid(cl_1), centroid(cl_2)
Px = (center_1[0]+center_2[0])/2*10000
Py = (center_1[1]+center_2[1])/2*10000
print(Px, Py)