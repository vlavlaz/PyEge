#Алгоритм перевода числа x в любую до 37 системы счисления
print("crackEGE --> ON")

BIG_NUM = 4294967296
alf: str = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def cs_conv(x, to_counting_system):
    res = ""
    neg = ""
    if to_counting_system >= 63 or to_counting_system <= 0:
        print(to_counting_system + "not supported CS")
        return -1
    if x < 0:
        neg = "-"
        x = abs(x)
    elif x == 0:
        return 0
    while x > 0:
        res += alf[x % to_counting_system]
        x //= to_counting_system
    res = neg+res
    return res

def digSUM(number):
    summ = 0
    strber = str(number)
    if int(number) == 0:
        return 0
    elif strber[0] == 0:
        strber = strber[2:]
    for x in strber:
        summ += alf.index(x)
    return summ

def digMULT(number):
    mult = 1
    strber = str(number)
    if int(number) == 0:
        return 0
    elif strber[0] == 0:
        strber = strber[2:]
    for x in strber:
        mult *= alf.index(x)
    return mult


