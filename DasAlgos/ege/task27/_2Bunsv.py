#https://education.yandex.ru/ege/task/757b3d4d-c16e-4181-a3e6-103d96b426fe
class Vacation:
    min_pay = 0
    max_pay = 0
    def __init__(self, lst):
        self.iD = lst[0]
        self.name = lst[1]
        self.company = lst[2]
        self.city = lst[3]
        if not lst[4] == "": self.min_pay = int(lst[4])
        if not lst[5] == "": self.max_pay = int(lst[5])
        self.xp = lst[6]
        if not lst[6] == "": self.xp = int(lst[6])
        self.date = lst[7]
        self.req_skills = lst[8]
    def av_pay(self):
        if self.max_pay == 0:
            return self.min_pay
        elif self.min_pay == 0:
            return self.max_pay
        else: return ((self.max_pay+self.min_pay)/2)
    def isValid(self):
        if self.iD != ""\
                and self.name != ""\
                and self.company != ""\
                and self.city != ""\
                and self.xp != ""\
                and self.date != ""\
                and self.req_skills != "":
            return True
        else:
            return False
    def groups(self):
        return [int(self.av_pay()//50000), 10+int(self.xp//2)]
    def isNeighborFor(self, other):
        groups_self = self.groups()
        groups_other = other.groups()
        xp = abs(groups_self[0]-groups_other[0])
        pay = abs(groups_self[1]-groups_other[1])
        if 0<=xp<=1: return True
        if 0<=pay<=1: return True
        return False
    def show(self):
        print(self.iD, self.min_pay, self.max_pay, self.xp)
        return "---------------"
def findS(g_groups):
    S = 0
    for group in g_groups:
        for vac in group:
            if "Python" in vac.req_skills:
                S+=1
    return S
def findK(g_groups):
    all = 0
    for group in g_groups:
        all+=len(group)
    return all-findS(g_groups)
def isNeighbors(group_A, group_B):
    if len(group_A) == 0 or len(group_B) == 0:
        return False
    for vacA in group_A:
        for vacB in group_B:
            if not(vacA.isNeighborFor(vacB)):
                return False
    return True

fB = open("_2B.txt")
strokes = [stroke.split(";") for stroke in fB]
vacs = []
xps = []
mx_ps = []
#print(strokes)
for stroke in strokes:
    vac = Vacation(stroke)
    if vac.isValid(): vacs.append(vac)
for vac in vacs:
    xps.append(vac.xp)
    mx_ps.append(vac.max_pay)
print(max(mx_ps), max(xps))
### Первые 9 - ЗП, потом ОПЫТ
groups = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

for vac in vacs:
    vac.show()
    print(vac.groups())
    groups[vac.groups()[0]].append(vac)
    groups[vac.groups()[1]].append(vac)
for g in groups:
    print(len(g))
#task for B file
good_groups = []
#Ищем 2 разные группы по ЗП/ОПЫТУ,
# которые входят в одну и туже группу по ОПЫТУ/ЗП
for g_A in groups:
    c_B = 0
    if len(g_A) == 0: continue
    print(g_A[0].show())
    for g_B in groups:
        c_C = 0
        c_B+=1
        if g_A == g_B: continue
        if len(g_B) == 0: continue
        if c_B < 10: continue
        for g_C in groups:
            c_C+=1
            if g_A == g_C or g_B == g_C: continue
            if len(g_C) == 0: continue
            if c_C >= 10: continue
            if isNeighbors(g_A, g_B) and isNeighbors(g_A, g_C) and isNeighbors(g_B, g_C):
                good_groups = [g_A, g_B, g_C]
                break
print(good_groups[0][0].show())
print(good_groups[1][0].show())
print(good_groups[2][0].show())
print(findS(good_groups), findK(good_groups))