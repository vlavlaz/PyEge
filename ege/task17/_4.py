pairs, nums = [], []
with open("_4.txt") as f:
    for x in f:
        nums.append(int(x))
    for i in range(0, len(nums)-1):
        pairs.append([nums[i], nums[i+1]])
print(sorted(nums))
_sq2min = 132**2
def _1cond(pair):
    if pair[0]+pair[1] < 132**2:
        return True
    else:
        return False
ans = []
for pair in pairs:
    if _1cond(pair):
        ans.append(pair[0]+pair[1])
print(len(ans), max(ans))
