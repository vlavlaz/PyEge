#https://education.yandex.ru/ege/task/6a2e2ee9-21a1-40b9-a6d1-f57446214527
trios, nums = [], []
with open("_17.txt") as f:
    for x in f:
        nums.append(int(x))
    for i in range(0, len(nums)-2):
        trios.append([nums[i], nums[i+1], nums[i+2]])
print(trios)
max36 = 99828
def _1cond(trio):
    count = 0
    if trio[0] > 0 or abs(trio[0])%100==36:
        count+=1
    if trio[1] > 0 or abs(trio[1])%100==36:
        count+=1
    if trio[2] > 0 or abs(trio[2])%100==36:
        count+=1
    if count >= 2:
        return True
    else:
        return False
def _2cond(trio):
    if trio[0]+trio[1]+trio[2] <= 99828:
        return True
    else:
        return False
answ = []

for trio in trios:
    if _1cond(trio) and _2cond(trio):
        answ.append(trio[0]+trio[1]+trio[2])

print(len(answ), min(answ))