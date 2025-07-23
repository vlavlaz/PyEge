#https://education.yandex.ru/ege/task/3c40e64b-b5e2-4c2f-b4a4-7be30bb6f3b9
strokes = []
with open("_7.txt") as f:
    for s in f:
        stroke = s.split("\t")
        for i in range(4):
            stroke[i] = int(stroke[i])
        strokes.append(stroke)
def valid(stroke):
    uniq = []
    for x in stroke:
        if x not in uniq:
            uniq.append(x)
    if len(uniq)==2 or len(uniq)==1:
        return True
    else:
        return False
cnt = 0
for s in strokes:
    if valid(s):
       cnt+=1
print(cnt)