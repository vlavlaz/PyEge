#https://education.yandex.ru/ege/task/cbdb41bb-8a06-4dba-b51b-fe33a0be57d0
f = open("_17.txt")
nums = [int(x) for x in f]
pairs = []
sus = []

def findMax4(nums):
    mx = 0
    for num in nums:
        c = str(num)
        if len(c) == 4 and mx < num:
            mx = num
    return mx
mx4 = findMax4(nums)

def _cond(pair, mx4):
    if abs(pair[0]-pair[1]) >= mx4:
        return True
    else:
        return False

for i in range(0, len(nums)-1):
    pairs.append([nums[i], nums[i+1]])
for pair in pairs:
    if _cond(pair, mx4):
        sus.append(pair[0]+pair[1])
print(len(sus), max(sus))

#CORRECT -> 49714 188759