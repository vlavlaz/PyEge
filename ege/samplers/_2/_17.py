nums, pairs =[], []
with open("_17.txt") as f:
    for x in f:
        nums.append(int(x))
    for i in range(0, len(nums)-1):
        pairs.append([nums[i], nums[i+1]])
for x in sorted(nums):
    if x > 0 and x % 41 == 0:
        print(x)
        break

mn41 = 41
ans = []
for p in pairs:
    if p[0]!=p[1] and abs(p[0]-p[1])%41==0:
        ans.append(p[0]+p[1])
print(len(ans), max(ans))
#print(pairs)