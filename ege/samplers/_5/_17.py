trios, nums = [], []
with open("_17.txt") as f:
    for x in f:
        nums.append(int(x))
    for i in range(0, len(nums)-2):
        trios.append([nums[i], nums[i+1], nums[i+2]])
that_el = 79971
print(sorted(nums))
def triosum(t):
    return t[0]+t[1]+t[2]
def valid(t):
    if triosum(t) > 79971:
        return False
    cnt = 0
    if t[0]%2==0:
        cnt+=1
    if t[1]%2==0:
        cnt+=1
    if t[2]%2==0:
        cnt+=1
    if cnt == 3:
        return False
    return True
ans = []
for t in trios:
    if valid(t):
       ans.append(triosum(t))
print(len(ans), max(ans))
