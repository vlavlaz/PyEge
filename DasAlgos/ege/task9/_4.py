#https://education.yandex.ru/ege/task/685ba6c3-5599-4049-9ecf-5356be796519
strokes = []
with open("_4.txt") as f:
    for stroke in f:
        stroke = stroke.replace(",", ".")
        if stroke != []:
            strokes.append(stroke.split())

count = 0
for stroke in strokes:
    if float(stroke[0])-float(stroke[1])>=5 and (0<=int(stroke[2])<=45 or 315<=int(stroke[2])<=360):
        count += 1
        print(stroke)
print(count)
