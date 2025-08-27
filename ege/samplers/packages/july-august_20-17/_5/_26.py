data = []
with open ("_26.txt") as f:
    for l in f:
        data.append(list(map(int,l.split())))
nums = []
id_time = {}
cur_id = 1
for d in data:
    id_time[cur_id] = [min(d), min(d)==d[0]]
    cur_id+=1
    for x in d:
        nums.append(x)
sorted_nums = sorted(nums)
print(sorted_nums)


