#https://education.yandex.ru/ege/task/65bc5b5a-439d-4f2e-b1cd-c6927ace1c2d

from EGE import *
def algo(N):
    st = str(N).replace("3", "4")
    st = st.replace("7", "8")
    return digMULT(st)

for N in range(1000, 10000):
    N = str(N)
    if N.count("0") > 0 or N.count("2") > 0 or N.count("4") > 0 or N.count("5") > 0 or N.count("8") > 0:
        continue
    else:
        R = algo(N)
        if R == 256:
            print(N)
            break

#1377 -> CORRECT
