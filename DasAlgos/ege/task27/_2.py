#https://education.yandex.ru/ege/task/757b3d4d-c16e-4181-a3e6-103d96b426fe
class vacation:
    def __init__(self, lst):
        self.iD = lst[0]
        self.name = lst[1]
        self.company = lst[2]
        self.city = lst[3]
        self.min_pay = lst[4]
        self.max_pay = lst[5]
        self.xp = lst[6]
        self.date = lst[7]
        self.req_skills = lst[8]
fA = open("_2A.txt")
strokes = [stroke.split(";") for stroke in fA]
vacs = []
q_uniq = []
print(strokes)
for stroke in strokes:
    vacs.append(vacation(stroke))

