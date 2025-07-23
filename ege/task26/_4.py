#https://education.yandex.ru/ege/task/a1b96fa1-7cf5-4a10-aa78-e933372024a2
f = open("_4.txt")
nums = [int(x) for x in f]
chairs_amount = 5179
players_amount = 8179
p_cord, c_cord = [], []
for i in range(chairs_amount):
    c_cord.append(nums[i])
for i in range(chairs_amount, chairs_amount + players_amount):
    p_cord.append(nums[i])
champ_chair = {}
c_cord.sort(); p_cord.sort()
















#Для каждого стула мы ищем всех притендетов на него. Среди всех притендентов выбираем ближайшего и сохраняем в словарь. Выбиваем из координат игроков всех претендентов.
### ТЯЖЕЛО
for chair in c_cord:
    print(chair)
    champ = 99999999999
    challengers = []
    for player in p_cord:
        closest_chair = 999999999999
        for potential_chair in c_cord:
            check_chair = abs(potential_chair - player)
            if closest_chair > check_chair:
                closest_chair = check_chair
        if chair == closest_chair:
            challengers.append(player)
    for player in challengers:
        if player-chair < champ-chair:
            champ = player
        p_cord.remove(player)
    champ_chair[champ] = chair
print(champ_chair)




