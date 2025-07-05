class Point:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def dance(self, other):
        return ((self.x**2-other.x**2) + (self.y-other.y)**2)**0.5
    def print(self):
        print(self.x, self.y, end="")
def x_cord(y_cord, points):
    xs = []
    for p in points:
        if p.y == y_cord:
            xs.append(p.x)
    return xs
def y_cord(x_cord, points):
    ys = []
    for p in points:
        if p.y == x_cord:
            ys.append(p.y)
    return ys
def solveForPair(p_1, p_2):
    points, ex, ey = [], [], []
    for p1, p2 in p_1, p_2:
        points.append(Point(p1,p2))
        ex.append(p1)
        ey.append(p2)
    l_border = Point(min(ex), min(y_cord(min(ex), points)))
    r_border = Point(max(ex), min(y_cord(max(ex), points)))
    b_border = Point(min(ey), min(y_cord(min(ey), points)))
    t_border = Point(max(ey), min(y_cord(max(ey), points)))
    l_border.print()
    r_border.print()
    b_border.print()
    t_border.print()
    claster_1 = []
    claster_2 = []
    claster_3 = []

fA = open("_3A.txt")
strokes = [stroke.split() for stroke in fA]
l = len(strokes)
p1, p2, p3, p4, p5 = [], [], [], [], []
for i in range (l):
    p1.append(float(strokes[i][0]))
    p2.append(float(strokes[i][1]))
    p3.append(float(strokes[i][2]))
    p4.append(float(strokes[i][3]))
    p5.append(float(strokes[i][4]))
params = [p1, p2, p3, p4, p5]
for i in range (5):
    for j in range (i+1, 5):
        solveForPair(params[i], params[j])
## СЛИШКОМ ЛЮТЫЕ ЗАДАНИЯ ДЛЯ МЕНЯ ПОКА, БУДУ ЖДАТЬ РАЗБОРОВ
