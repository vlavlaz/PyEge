#https://education.yandex.ru/ege/task/0cee3383-2699-4e0d-a2f1-5f50a85ad086

def sec_cond(a, b, c, d):
    trgt = (a+b+c+d)/2
    if a+b == trgt or a+c == trgt or a+d == trgt or b+c == trgt or b+d == trgt or c+d == trgt:
        return True
    else: return False

f = open("_1.txt")
nums = []

for strr in f:
    strr = strr.split("\t")
    for x in strr:
        nums.append(int(x))

count = 0

for i in range (0, len(nums)-3, 4):
    mx = max(nums[i], nums[i+1], nums[i+2], nums[i+3])
    su = nums[i] + nums[i+1] + nums[i+2] + nums[i+3]
    if mx < su - mx and sec_cond(nums[i], nums[i+1], nums[i+2], nums[i+3]):
        count+=1
print(count)
#116 -> CORRECT
