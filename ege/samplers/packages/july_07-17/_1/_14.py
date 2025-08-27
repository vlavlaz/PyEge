#https://education.yandex.ru/ege/task/08f6e0f1-0ce1-42d4-a73e-2e9d1e334a55
alf = "0123456789abcdefg"
for x in alf:
    a = int("5432" + x + "67" , 17)
    b = int("302" + x, 17)
    if (a+b)%19==0:
        print(a+b)