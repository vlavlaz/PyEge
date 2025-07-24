#https://education.yandex.ru/ege/task/6488e44b-c19d-41be-a53f-3877c2d12728
nums, pairs = [], []
with open("_17.txt") as f:
    for x in f:
        nums.append(int(x))
    for i in range(0, len(nums)-1):
        pairs.append([nums[i], nums[i+1]])
def sp(pair):
    return pair[0]+pair[1]
def _1cond(pair1, pair2, pair3):
    if sp(pair2) > sp(pair1) and sp(pair2) > sp(pair3):
        return True
    else:
        return False
def _2cond(pair1, pair2, pair3):
    if  sp(pair1) > 0 and \
        sp(pair2) > 0 and \
        sp(pair3) > 0:
        return True
    else:
        return False
print(pairs)
ans = []
for i in range(0, len(pairs)-4):
    if _1cond(pairs[i], pairs[i+2], pairs[i+4]) and _2cond(pairs[i], pairs[i+2], pairs[i+4]):
        ans.append(pairs[i+2][0]*pairs[i+2][1])
print(len(ans), min(ans))
