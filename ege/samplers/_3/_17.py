trios, nums = [], []
with open("_17.txt") as f:
    for x in f:
        nums.append(int(x))
    for i in range(0, len(nums)-2):
        trios.append([nums[i], nums[i+1], nums[i+2]])
mn = 10125
def _1cond(trio):
    cnt = 0
    if trio[0]%mn == 0:
        cnt+=1
    if trio[1]%mn == 0:
        cnt+=1
    if trio[2]%mn == 0:
        cnt+=1
    if cnt >= 1:
        return True
    else:
        return False
def s(trio):
    return trio[0] + trio[1] + trio[2]
def _2cond(trio):
    if len(str(s(trio))) == 6:
        return True
    else:
        return False
res= []
for trio in trios:
    if _1cond(trio) and _2cond(trio):
        res.append(s(trio))
print(len(res), max(res))
