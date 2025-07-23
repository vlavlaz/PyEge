strokes = []
with open("_5.txt") as f:
    for stroke in f:
        _stroke = stroke.split()
        strokes.append([_stroke[0], int(_stroke[1]), int(_stroke[2])])
studs = []
stud_time_amount = {}
times = []
amounts = []
for i in range(len(strokes)):
    if strokes[i][1] not in studs:
        studs.append(strokes[i][1])
        last_time = ""
        solved = []
        for stroke in strokes:
            if stroke[1] == strokes[i][1] and stroke[2] not in solved:
                solved.append(stroke[2])
                last_time = stroke[0]
        stud_time_amount[strokes[i][1]] = [last_time, len(solved)]
        if len(solved) == 15:
            print(strokes[i][0], strokes[i][1])
        amounts.append(len(solved))

