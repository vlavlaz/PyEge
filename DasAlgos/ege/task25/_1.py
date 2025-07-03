#https://education.yandex.ru/ege/task/2135bad3-5844-4cbd-8a72-93751f24130f
# mask = 1*28?64 == 1____28x64, x E [0, 9]

from fnmatch import fnmatch
mask = "1*28?64"

def sec_cond(x):
    count = 0
    for d in range(1, 10):
        if x%int(str(d)+"4") == 0: count += 1
    if count == 5: return True
    else: return False

for n in range(128092, 2*10**9, 124):
    if sec_cond(n):
        if fnmatch(str(n), mask):
            print(n, n//124)

print("DEAD")
#118328364 954261
#1065728664 8594586
#1111428864 8963136
#1241628864 10013136
#1384328064 11163936
#1514528064 12213936
#1605928464 12951036
#1697328864 13688136 --> CORRECT

#vvvvvvvvvTRUE_CHAD_SOLUTIONvvvvvvvvv
def mask(x):
    for d in range(0, 10):
        strber = "128" + str(d) + "64"
        if int(strber) == x: return True
    for d in range(0, 10):
        for s in ["0", "00", "000", "0000"]:
            strber = "1" + s + "28" + str(d) + "64"
            if int(strber) == x: return True
        for s in range(1000, 10000):
            strber = "1" + str(s) + "28" + str(d) + "64"
            if int(strber) == x: return True
        for s in range(100, 1000):
            for z in range (0, 2):
                strber = "1" + "0"*z + str(s) + "28" + str(d) + "64"
                if int(strber) == x: return True
        for s in range(10, 100):
            for z in range (0, 3):
                strber = "1" + "0"*z + str(s) + "28" + str(d) + "64"
                if int(strber) == x: return True
        for s in range(0, 10):
            for z in range (0, 4):
                strber = "1" + "0"*z + str(s) + "28" + str(d) + "64"
                if int(strber) == x: return True
    return False

mask_check = []
for n in range (128092, 1999928964, 124):
    if sec_cond(n):
        mask_check.append(n)
print("SEC_DONE")
answer = []
for n in mask_check:
    if mask(n):
        answer.append(n)
        answer.append(n//124)
        print(n, n // 124)
