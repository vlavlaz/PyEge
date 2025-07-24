#https://education.yandex.ru/ege/task/7595fc66-a7ba-47d7-885e-17db99cf2811
data = []
with open("_2.txt") as f:
    for X in f:
        s = X.split()
        data.append([int(s[0]), int(s[1])])
rows = {}
good_rows = {}
for X in data:
    if not X[0] in rows.keys():
        rows[X[0]] = []
for X in data:
    rows[X[0]].append(X[1])
for row, trees in rows.items():
    if len(trees) < 2:
        continue
    for i in range(len(trees)):
        for j in range(i+1, len(trees)):
            if abs(trees[i]-trees[j]) == 14:
                if not row in good_rows.keys():
                    good_rows[row] = [[trees[i], trees[j]]]
                else:
                    good_rows[row].append([trees[i], trees[j]])
sorted_good = sorted(good_rows.keys())
print(sorted_good[-1], sorted(good_rows[sorted_good[-1]][0]))
