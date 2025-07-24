#https://education.yandex.ru/ege/task/757b3d4d-c16e-4181-a3e6-103d96b426fe
class Vacation:
    min_pay = 0
    max_pay = 0
    req_skills = []
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
        else: return (self.max_pay + self.min_pay)/2
    def isValid(self):
        pay_flag = False
        if self.min_pay == 0 and self.max_pay != 0: pay_flag = True
        elif self.max_pay == 0 and self.min_pay != 0: pay_flag = True
        elif self.min_pay <= self.max_pay: pay_flag = True
        if self.iD != ""\
                and self.name != ""\
                and self.company != ""\
                and self.city != ""\
                and self.xp != ""\
                and self.date != ""\
                and self.req_skills != "\n"\
                and pay_flag:
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
        if 0<xp<=1: return True
        if 0<pay<=1: return True
        return False
    def show(self):
        print(self.iD, self.name, self.company, self.city, self.min_pay, self.max_pay, self.xp, self.date, self.req_skills, end="")
def findSK(g_groups):
    S = 0
    uniq_vacs = []
    suka = 0
    for group in g_groups:
        suka+=len(group)
        for vac in group:
            if not vac in uniq_vacs:
                uniq_vacs.append(vac)
                if "Python" in vac.req_skills:
                    S+=1
    K = suka - S
    return [S, K]

def uniq(g_groups):
    uniq_vacs = []
    for group in g_groups:
        for vac in group:
            if not vac in uniq_vacs:
                uniq_vacs.append(vac)
    return len(uniq_vacs)
def isNeighbors(group_A, group_B):
    if len(group_A) == 0 or len(group_B) == 0:
        return False
    for vacA in group_A:
        for vacB in group_B:
            if not(vacA.isNeighborFor(vacB)):
                return False
    return True

fA = open("_2A.txt")
strokes = [stroke.split(";") for stroke in fA]
vacs = []
xps = []
mx_ps = []
print(strokes)
for stroke in strokes:
    vac = Vacation(stroke)
    if vac.isValid() and not (vac in vacs):
        vac.show()
        vacs.append(vac)
for vac in vacs:
    xps.append(vac.xp)
    mx_ps.append(vac.max_pay)
### Первые 10 - ЗП, потом ОПЫТ
groups = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
for vac in vacs:
    groups[vac.groups()[0]].append(vac)
    groups[vac.groups()[1]].append(vac)
#task for A file
mx_su = 0
good_groups = []
for i in range(len(groups)):
    for j in range(len(groups)):
        if isNeighbors(groups[i], groups[j]):
            su = len(groups[i]) + len(groups[j])
            if su > mx_su:
                good_groups = [groups[i], groups[j]]
                mx_su = su
                print(findSK(good_groups))

#В РОТ ЭТО ЗАДАНИЕ _2, ХУЙНЯ УСЛОВИЕ, ХУЙНЯ ЗАДАНИЕ



