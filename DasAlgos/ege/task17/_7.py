pairs, nums = [], []
with open("_7.txt") as f:
    for x in f:
        nums.append(int(x))
    for i in range(0, len(nums)-1):
        pairs.append([nums[i], nums[i+1]])
print(sorted(nums))
mx__ = 94
def _1cond(pair):
    if len(str(pair[0])) == 2 or len(str(pair[1])) == 2:
        return True
    else:
        return False
def _2cond(pair):
    if pair[0] + pair[1] <= 94:
        return True
    else:
        return False
ans = []
for pair in pairs:
    if _1cond(pair) and _2cond(pair):
       ans.append(pair[0]+pair[1])
print(len(ans), max(ans))