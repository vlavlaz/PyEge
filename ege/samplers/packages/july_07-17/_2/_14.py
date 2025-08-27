#https://education.yandex.ru/ege/task/e07ffce3-c3fb-4aad-933f-4291ee998760
alf = "0123456789abcd"
for x in alf:
    for y in alf:
        a = int("14"+y+"5"+x+"2", 14)
        b = int("31"+x+"2"+y+"3", 14)
        if (a+b)%9 == 0:
            print("X, Y:", x, y, "SU:", int(x,14)+int(y,14), "DEL:", (a+b)//9)