#https://education.yandex.ru/ege/task/568e6793-fe55-44eb-8e94-17787b5a6853

f = open("_2.txt")
nums = [int(x) for x in f]
min11 = 211
def is3d(x):
    if len(str(x)) == 3: return True
    else: return False
def _1cond(a, b):
    if is3d(a) and not(is3d(b)) or is3d(b) and not(is3d(a)): return True
    else: return False
def _2cond(a, b):
    if abs(a - b) % 211 == 0: return True
    else: return False
sus = []
for i in range(0, len(nums)-1):
    if _1cond(nums[i], nums[i+1]) and _2cond(nums[i], nums[i+1]):
        sus.append(nums[i]+nums[i+1])
print(len(sus), max(sus))

#8 8089 --> CORRECT
#for x in nums:
#    if is3d(x) and x%100==11 and min11>x:
#        min11 = x
#print(min11) --> 211


