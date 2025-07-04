#https://education.yandex.ru/ege/task/a0ce5e2d-339e-4fb8-8953-4f4f5b3f93a0

class Point:
    def __init__(self, x, y):
        self.X = x
        self.Y = y
    def dance(self, other):
        return ((other.X - self.X)**2+(other.Y - self.Y)**2)**0.5
    def danceX(self, other):
        return abs(self.X - other.X)
    def danceY(self, other):
        return abs(self.Y - other.Y)
    def show(self):
        print(self.X, self.Y)
def X_cord(Y_cord, points):
    for i in range(len(points)):
        if Y_cord == points[i].Y:
            return points[i].X
    return "I refuse to work with you"

def Y_cord(X_cord, points):
    for i in range(len(points)):
        if X_cord == points[i].X:
            return points[i].Y
    return "I refuse to work with you"

def sum_dance(p, claster):
    su = 0
    for other_p in claster:
        su += p.dance(other_p)
    return su
def claster_center(claster):
    center = Point
    center_su = sum_dance(claster[0], claster)
    for p in claster:
        check = sum_dance(p, claster)
        if check < center_su:
            center_su = check
            center = p
    return center
def maXdist(claster):
    center = claster_center(claster)
    mx = 0
    for p in claster:
        if mx < p.danceX(center):
            mx = p.danceX(center)
    return mx
def maYdist(claster):
    center = claster_center(claster)
    my = 0
    for p in claster:
        if my < p.danceY(center):
            my = p.danceY(center)
    return my
f = open("_1A.txt")
strokes = [stroke.split() for stroke in f]
l = len(strokes)
points = []
Ex = []
Ey = []
claster_1 = []
claster_2 = []
H = W = 3
for i in range (l):
    points.append(\
        Point(float(strokes[i][0]), float(strokes[i][1]))\
        )
    Ex.append(points[i].X)
    Ey.append(points[i].Y)
X_max = max(Ex)
Y_max = max(Ey)
X_min = min(Ex)
Y_min = min(Ey)
for p in points:
    if p.X > X_max-W and p.Y > Y_max-H:
        claster_1.append(p)
    elif p.X < X_min+W and p.Y < Y_min+H:
        claster_2.append(p)
    else: print("EXHAUST:", p.X, p.Y)

print(int(maXdist(claster_1)*10000), int(maYdist(claster_1)*10000))
print(int(maXdist(claster_2)*10000), int(maYdist(claster_2)*10000))

f1 = open("_1Б.txt")
strokes1 = [stroke.split() for stroke in f1]
l = len(strokes1)
points = []
Ex = []
Ey = []
claster_3 = []
claster_4 = []
claster_5 = []
H = W = 3
for i in range (l):
    points.append(\
        Point(float(strokes1[i][0]), float(strokes1[i][1]))\
        )
    Ex.append(points[i].X)
    Ey.append(points[i].Y)
X_max = max(Ex)
Y_max = max(Ey)
X_min = min(Ex)
Y_min = min(Ey)
print(X_max, Y_cord(X_max, points))
print(X_cord(Y_max, points), Y_max)
print(X_min, Y_cord(X_min, points))
print(X_cord(Y_min, points), Y_min)
for p in points:
    if p.X <= X_max-W and p.Y >= Y_max-H:
        claster_3.append(p)
    elif p.X <= X_min+W and p.Y <= Y_min+H:
        claster_4.append(p)
    else:
        claster_5.append(p)

print(int(maXdist(claster_3)*10000), int(maYdist(claster_3)*10000))
print(int(maXdist(claster_4)*10000), int(maYdist(claster_4)*10000))
print(int(maXdist(claster_5)*10000), int(maYdist(claster_5)*10000))

#14749, 14299
#12891, 14700





