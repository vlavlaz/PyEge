#https://education.yandex.ru/ege/task/f4f17581-c911-4ab0-9a72-a70827259b20
def valid(s):
    uniq = ""
    for x in s:
        if x not in uniq:
            uniq+=x
        else:
            return False
    return True
for N in range(1000, 100000):
    temp = str(N)
    if not valid(temp): continue
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
    temp = temp.replace(mx, "", 1)
    temp = temp.replace(mn, "", 1)
    mu = 1
    for x in temp:
        mu*=int(x)
    su = int(mn) + int(mx)
    sus = str(su); mus = str(mu)
    R = ""
    if su <= mu:
        R = sus + mus
    else:
        R = mus + sus

    print(N, mn, mx, sus, mus, R)

    if int(R) > 85:
        print(N, int(R))
        break
