#https://education.yandex.ru/ege/task/f4f17581-c911-4ab0-9a72-a70827259b20
for N in range(100000):
    temp = str(N)
    mx, mn = "0", "999"
    mxi, mni = 0, 0
    i = 0
    for c in temp:
        if int(mx) <= int(c):
            mxi = i
            mx = c
        if int(mn) >= int(c):
            mn = c
            mni = i
        i+=1
    su = 0
    mu = 1
    for x in temp:
        su += int(x)
        mu *= int(x)
    if temp[mni]!= "0": mu = mu//int(temp[mni])//int(temp[mxi])
    su = su - int(temp[mni]) - int(temp[mxi])
    sus = str(su); mus = str(mu)
    R = ""
    if su <= mu:
        R = sus + mus
    else:
        R = mus + sus
    if int(R) > 85:
        print(N, int(R))
        break
