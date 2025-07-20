strokes1 = []
strokes2 = []
with open("csv.txt") as f:
    for s in f:
        stroke = s.split("\t")
        for i in range(0, len(stroke)):
            stroke[i] = int(stroke[i])
        strokes1.append(stroke)
with open("xls.txt") as f1:
    for s in f1:
        stroke = s.split("\t")
        for i in range(0, len(stroke)):
            stroke[i] = int(stroke[i])
        strokes2.append(stroke)
missed = 0
for i in range (0, len(strokes1)):
    if strokes1[i] != strokes2[i]:
        print(strokes1[i], strokes2[i], "<------", i)
        missed+=1
print(missed, "<----- different strokes")