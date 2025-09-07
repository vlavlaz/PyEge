#https://education.yandex.ru/ege/task/ca5aa6d7-cc1a-4f63-bc1f-cbfa83fa2f9c
data = {}
nums = []
with open("_26.txt") as f:
    c = 1
    for l in f:
        d = list(map(int, l.split()))
        for x in d:
            nums.append(x)
        data[d[0]] = [d[1], 1 if min(d) == d[0] else 0, c]
        c+=1
head, end = {}, {}
cnt = 1
for x in sorted(data.keys()):
    if data[x][1] and not (data[x][2] in head.values() or data[x][2] in end.values()):
        head[cnt] = data[x][2]
    elif not (data[x][2] in head.values() or data[x][2] in end.values()):
        end[cnt] = data[x][2]
    cnt+=1
print(len(end))
