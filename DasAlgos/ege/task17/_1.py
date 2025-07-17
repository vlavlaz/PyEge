# https://education.yandex.ru/ege/task/9e1238d3-5ea2-4d41-8aec-816b627cdf6b

f = open("_1.txt")
nums = [int(x) for x in f]
mx3 = 0
for x in nums:
    if mx3 <= x and 0<x//100<10:
        mx3 = x
def _1cond(a, b):
    ad = len(str(a))
    bd = len(str(b))
    if (ad == 3 and bd != 3 or ad != 3 and bd == 3): return True
    else: return False
def _2cond(a, b, mx):
    if a + b >= mx: return True
    else: return False
count = 0
apr = []
for i in range(0, len(nums)-1):
    if _1cond(nums[i], nums[i+1]) and _2cond(nums[i], nums[i+1], mx3):
       apr.append(nums[i]+nums[i+1])
print(len(apr), max(apr)) #1657 10962 --> CORRECT

