def has11 (s):
    if "11" in s: return True
    else: return False
def has444 (s):
    if "444" in s: return True
    else: return False
def has8888 (s):
    if "8888" in s: return True
    else: return False

ANS = 0
from DasAlgos.EGE import *
for n in range (4, 10001):
    buz = "8" + "4" * n
    #pragma
    while has11(buz) or has444(buz) or has8888(buz) :
        if has11:
            buz = buz.replace("11", "4", 1)
        if has444:
            buz = buz.replace("444", "88", 1)
        if has8888:
            buz = buz.replace("8888", "1", 1)
    #pragma_end
    check = digSUM(buz)
    if check > ANS:
        print(check, ANS, n)
        ANS = check
print(ANS)