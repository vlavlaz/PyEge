#https://education.yandex.ru/ege/task/ac407c00-8ed4-46fb-b78c-45b5ebcd9b6d
pairs = []
with open("_17.txt") as f:
    nums = []
    for x in f:
        nums.append(int(x))
    for i in range(0, len(nums)-1):
        pairs.append([nums[i], nums[i+1]])
max_3 = 968**3
def sumDIG(x):
    if x >= 0: c = str(x)
    else: c = str(x)[1:]
    sum = 0
    for y in c:
        sum += int(y)
    return sum
def _1cond(pair):
    if sumDIG(pair[0]) %5 == 0 and sumDIG(pair[1]) %5 != 0:
        return True
    elif sumDIG(pair[1]) %5 == 0 and sumDIG(pair[0]) %5 != 0:
        return True
    else:
        return False
def _2cond(pair):
    if abs(pair[0]**2-pair[1]**2)>=968**3:
        return True
    else:
        return False
answ = []
for pair in pairs:
    if _1cond(pair) and _2cond(pair):
        answ.append(pair[0] + pair[1])
print(len(answ), max(answ))