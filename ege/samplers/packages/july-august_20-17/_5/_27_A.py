import pandas as pd
import matplotlib.pyplot as plt
def distance(x1,x2,y1,y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5
def center(claster):
    mn = 999999999
    centroid = []
    for cord in claster:
        sud = 0
        for check in claster:
            sud += distance(cord[0], check[0], cord[1], check[1])
        if mn > sud:
            mn = sud
            centroid = cord
    return centroid

cords = []
with open("_27_А.txt") as f:
    for x in f:
        cords.append(list(map(float, x.split())))
claster1 = [cord for cord in cords if 10<=cord[0]<=30 and 10<=cord[1]<=40.5]
claster2 = [cord for cord in cords if 50<=cord[0]<=70 and 59<=cord[1]<=80.5]
ctr1 = center(claster1)
ctr2 = center(claster2)
Px = (ctr1[0]+ctr2[0])/2*10000
Py = (ctr1[1]+ctr2[1])/2*10000
print(Px, Py)


X = [cord[0] for cord in cords]
Y = [cord[1] for cord in cords]
data = {
    "X": X,
    "Y": Y
}
df = pd.DataFrame(data)
print(df)
plt.figure(figsize=(10, 6))
plt.scatter(df["X"], df["Y"], color="blue", edgecolor="black", alpha=0.7)
plt.show()