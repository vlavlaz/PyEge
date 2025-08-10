nums, quatros = [], []
with open("_17.txt") as f:
    for x in f:
        nums.append(int(x))
    for i in range(0, len(nums)-3):
        quatros.append([nums[i], nums[i+1], nums[i+2], nums[i+3]])
min2025 = 12150
def _1cond(quad):
    if quad[0] > 0 and quad[3] > 0:
        return True
    else:
        return False
def _2cond(quad):
    if abs(quad[2] + quad[3]) <= 12150:
        return True
    else:
        return False
ans = []
for quad in quatros:
    if _1cond(quad) and _2cond(quad):
        ans.append(quad[0]+quad[1]+quad[2]+quad[3])
print(len(ans), min(ans))