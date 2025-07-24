#https://education.yandex.ru/ege/task/062a4793-f5f9-4b96-be39-1a81c87197f3
eq = 18*7**108 - 5*49**76 + 343**35 - 50
def sumd(x):
    alf = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLM"
    su = 0
    for a in x:
        if a!= "-": su += alf.index(a)
    return su
def to49(x1):
    alf = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLM"
    res = ""
    x = abs(x1)
    while x > 0:
        res += alf[x%49]
        x//=49
    return res[::-1]
print(sumd(to49(eq)))

