#Арифметическое выражение уже в N-системе счисления.

alf = "0123456789abcde"
for y in alf:
    a = int("ABCD" + y, 15)
    b = int("123"+y+"4", 15)
    su = a+b
    if su%14 == 0:
        print(su//14)
#43166 -> CORRECT Халявка