#https://education.yandex.ru/ege/task/9f4359b3-ef2f-4ea1-9b54-69920791d9a3
f = open("_2.txt")
nums = []

for strr in f:
    strr = strr.split()
    for x in strr:
        nums.append(int(x))
def _1cond(a, b, c):
    if a < b and b < c: return True
    else: return False
def _2cond(a, b, c):
    if a != b and b != c and a != c: return True
    else: return False

count = 0
for i in range(0, len(nums), 3):
    if _1cond(nums[i], nums[i+1], nums[i+2]) and _2cond(nums[i], nums[i+1], nums[i+2]):
        count+=1
print(count)

