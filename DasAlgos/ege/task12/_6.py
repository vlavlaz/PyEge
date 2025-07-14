#https://education.yandex.ru/ege/task/6b569580-7aaf-419c-b554-fd2b7f1afbce
def algo(s1):
    s = str(s1)
    while "53" in s or "63" in s:
        if "63" in s:
            s = s.replace("63", "72", 1)
        else:
            s = s.replace("53", "91", 1)
    return s

print(algo("53"*25+"63"*15+"6"*5))
print(25*10+9*15+6*5)