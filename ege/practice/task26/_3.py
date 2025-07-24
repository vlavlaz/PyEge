# https://education.yandex.ru/ege/task/2fde956d-cb4f-40b7-8699-5a1fdfbbe9a8
f = open("_3.txt")
strokes = [stroka.split() for stroka in f]
sts = []
ends = []
durs = []
#print(strokes)
l = len(strokes) - 1
work_time = int(strokes[0][0])
bids = int(strokes[0][1]) #Заявок
for i in range(1, l+1):
    sts.append(int(strokes[i][0]))
    ends.append(int(strokes[i][1]))
    durs.append(int(ends[i-1]-sts[i-1]))
#Ищем мероприятие чей конец - длительность совпадает с концом пред события, при этом минимизируя текущий искомый конец
end_dur = {}
for i in range(0, l):
    min_dur = durs[i]
    for j in range(i+1, l):
        if ends[i] == ends[j] and min_dur > durs[j]:
            min_dur = durs[j]
    if not(ends[i]) in end_dur.keys() :
        end_dur[ends[i]] = min_dur
print(end_dur)
#Будем бегать пока не найдем окончание подходящее под нашу длительность:
# Теперь одному концу соответствует одна лучшая длительность, тогда
sorted_ends = sorted(ends)
def max_konf(first_end_p, sorted_ends, end_dur):
    time = first_end_p
    k = 1
    for opt_end in sorted_ends:
        if opt_end - end_dur[opt_end] >= time:
            while not (time == opt_end - end_dur[opt_end]):
                time += 1
            time += end_dur[opt_end]
            k += 1
    return k
def schedule(first_end_p, sorted_ends, end_dur):
    time = first_end_p
    desk = str(first_end_p)
    for opt_end in sorted_ends:
        if opt_end - end_dur[opt_end] >= time:
            while not (time == opt_end - end_dur[opt_end]):
                time += 1
            time += end_dur[opt_end]
            desk += " - " + str(opt_end) +"; " + str(opt_end)
    return desk+" - END."
max_k = max_konf(sorted_ends[0], sorted_ends, end_dur)
print(schedule(sorted_ends[0], sorted_ends, end_dur))
for first_end in end_dur.keys():
    if max_konf(first_end, sorted_ends, end_dur) == 91:
        print(schedule(first_end, sorted_ends, end_dur))
print(9914 - end_dur[9914])