buy_list = []
with open("_5.txt") as f:
    for x in f:
        buy_list.append(int(x))
buy_list  = sorted(buy_list, reverse=True)
all_in_one, split = 0, 0
for x in range(0, 7500):
    all_in_one+=buy_list[x]
for x in  range(7500, 10000):
    all_in_one+= buy_list[x] / 2
print(all_in_one)
for x in range(0, 10000):
    if (x+1)%4 == 0: split+=buy_list[x]/2
    else: split+=buy_list[x]
print(split)