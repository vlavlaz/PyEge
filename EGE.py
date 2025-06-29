#Алгоритм перевода числа x в любую до 37 системы счисления
print("crackEGE --> ON")
def cs_conv(x, to_counting_system):
    res = ""
    neg = ""
    alf = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
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
    number = str(number)
    for x in number:
        summ += int(x)
    return summ

def digSUM(number, counting_system):
    summ = 0
    number = str(int(number, counting_system))
    for x in number:
        summ += int(x)
    return summ

