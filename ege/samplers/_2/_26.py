import matplotlib.pyplot as plt
cords, X, Y = [], [], []
with open("_26.txt") as f:
    for l in f:
        i = list(map(int, l.split()))
        cords.append(i)
        X.append(i[0]), Y.append(i[1])
X = sorted(X)
Y = sorted(Y)
home_w = {}
def weight(cord, X, Y):
    x = cord[0]
    y = cord[1]
    Yi = Y.index(y)
    Xi = X.index(x)
    wr, wl, wd, wu = 1,1,1,1
    if Yi+1 != 10000 and Yi > 0:
        yr = Y[Yi+1]
        wr = abs(yr - y)
        yl = Y[Yi-1]
        wl = abs(y - yl)
    if Xi + 1 != 10000 and Xi > 0:
        xd = X[Xi + 1]
        wd = abs(xd - x)
        xu = X[Xi - 1]
        wu = abs(x - xu)
    return wr+wl+wd+wu
ct = 0
for cord in cords:
    ct += 1
    print(ct)
    home_w[weight(cord, X, Y)] = cord

print(max(home_w.keys()),home_w[max(home_w.keys())])


