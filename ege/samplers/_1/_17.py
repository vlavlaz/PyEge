#https://education.yandex.ru/ege/task/016a50c3-055f-47bb-97f9-81636a06f793
nums, pairs = [], []
with open("_17.txt") as f:
    for x in f:
        nums.append(int(x))
    for i in range(0, len(nums)-1):
        pairs.append([nums[i], nums[i+1]])
min2 = 10
def valid(p):
    cnt = 0
    if 10 <= p[0] <= 99:
        cnt+=1
    if 10 <= p[1] <= 99:
        cnt += 1
    if cnt == 1 and (p[0]+p[1])%10==0:
        return True
    return False
answ = []
for pair in pairs:
    if valid(pair):
        answ.append(pair[0]+pair[1])
print(len(answ), max(answ))