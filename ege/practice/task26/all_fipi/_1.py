#https://education.yandex.ru/ege/task/ba452f56-bd43-4a4f-80dd-e326e1bf9edb
users = []
with open("_1.txt") as f:
    X = f.readline().split()
    free_space = int(X[0])
    for X in f:
        users.append(int(X))
sorted_users = sorted(users)
accepted = []
for a in sorted_users:
    if free_space - a  > 0:
        free_space -= a
        accepted.append(a)
    else:
        break
print(sorted_users)
print(len(accepted), max(accepted))