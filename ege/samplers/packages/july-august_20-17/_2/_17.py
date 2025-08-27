trios, nums = [], []
with open("_17.txt") as f:
    for x in f:
        nums.append(int(x))
    for i in range(0, len(nums)-2):
        trios.append([nums[i], nums[i+1], nums[i+2]])
def _1cond(trio):
    cnt = 0
    if len(str(abs(trio[0])))==4 and abs(trio[0]) %100 == 42:
        cnt+=1
    if len(str(abs(trio[1])))==4 and abs(trio[1]) % 100 == 42:
        cnt += 1
    if len(str(abs(trio[2])))==4 and abs(trio[2]) % 100 == 42:
        cnt += 1
    if cnt >= 2:
        return True
    else:
        return False
mx42 = 9642
def st(trio):
    return trio[0]+trio[1]+trio[2]
def _2cond(trio):
    if st(trio) > 9642:
        return True
    else:
        return False
answ = []
for trio in trios:
    if _1cond(trio) and _2cond(trio):
        answ.append(st(trio))
print(len(answ), max(answ))


