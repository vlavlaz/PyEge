#https://education.yandex.ru/ege/task/a1b96fa1-7cf5-4a10-aa78-e933372024a2
#WRONG
f = open("_4.txt")
nums = [int(x) for x in f]
chairs = 5179
players = 8179
p_cord, c_cord = [], []
for i in range(chairs):
    c_cord.append(nums[i])
for i in range(chairs, chairs+players):
    p_cord.append(nums[i])
pa_ch = {}
for player in p_cord:
    mn = 9999999999
    for chair in c_cord:
        if mn > abs(chair-player):
            mn = abs(chair-player)
    pa_ch[player] = mn
dist = []
for d in pa_ch.values():
    dist.append(d)
md = max(dist)
s = 0
for p in pa_ch.keys():
    if md == pa_ch[p]:
        print(p)
        s = p
for i in range(chairs, chairs+players):
    if nums[i] == s:
        print(i)

