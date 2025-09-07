#https://education.yandex.ru/ege/task/dbbdb2ae-7334-4be9-9fd0-5aa8e531c322
strokes = []
with open("_9.txt") as f:
    for l in f:
        strokes.append(list(map(int, l.split("\t"))))
def sustroke(s):
    return s[0]+s[1]+s[2]+s[3]+s[4]+s[5]+s[6]
def valid(stroke):
    s = stroke.copy()
    uniq = []
    for x in stroke:
        if x not in uniq:
            uniq.append(x)
            s.remove(x)
    if not (len(uniq) == 5 and s[0]==s[1]):
        return False
    su = -s[0]
    for x in uniq:
        su += x
    if su/4>s[0]:
        return False
    return True

for stroke in strokes:
    if valid(stroke):
        print(sustroke(stroke))
